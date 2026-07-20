"""Convert a whole folder of content packs, with cross-pack links + an index.

Single-pack conversion can't resolve links into other packs. The corpus builder
processes every pack together in two passes:

1. **Scan** — read each pack's TOC, assign a collision-free section filename and
   per-topic anchors, and record its root's ``parentid`` (the edge that links it
   to another pack). This yields a global ``itemid -> (section_file, anchor)``
   map and a pack-level parent/child tree.
2. **Render** — convert each pack's bodies with a resolver backed by that global
   map, so ``../../OtherPack/…`` links become ``Other Section.md#anchor``.

Finally an ``INDEX.md`` is written from the pack tree (a topic's ``TocParentId``
can point into another pack, so the ~800 packs form one hierarchy).
"""
from __future__ import annotations

import json
import os
import tempfile
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote

from . import extract as _extract
from .assemble import PackScan, _safe_filename, copy_images, render_section, scan_pack
from .links import make_corpus_resolver

_CHECKPOINT = ".siemens_checkpoint.json"


def _load_checkpoint(out_dir: str) -> set:
    path = os.path.join(out_dir, _CHECKPOINT)
    if not os.path.exists(path):
        return set()
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        return set(data.get("done", []))
    except (json.JSONDecodeError, OSError):
        return set()


def _save_checkpoint(out_dir: str, done: set) -> None:
    path = os.path.join(out_dir, _CHECKPOINT)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump({"done": sorted(done)}, fh)
    os.replace(tmp, path)


def discover_packs(root: str) -> List[str]:
    """Return pack sources under ``root``: ``*.zip`` files and extracted pack folders."""
    out: List[str] = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.isfile(path) and path.lower().endswith(".zip"):
            out.append(path)
        elif os.path.isdir(path) and os.path.exists(os.path.join(path, "Toc", "Default.xml")):
            out.append(path)
    return out


def _unique_name(base: str, pack: str, used_lower: set) -> str:
    """Pick a section filename unique **case-insensitively**, so packs whose
    titles differ only in case don't silently overwrite each other on
    case-insensitive filesystems (Windows/macOS)."""
    name = base or pack
    if name.lower() not in used_lower:
        return name
    candidate = f"{name} ({pack})"
    i = 1
    while candidate.lower() in used_lower:
        i += 1
        candidate = f"{name} ({pack}-{i})"
    return candidate


def _write_index(out_dir: str, scans: List[Tuple[PackScan, str]], id_to_pack: Dict[str, str]) -> str:
    """Write INDEX.md as a nested list following the pack-level parent tree."""
    by_pack: Dict[str, Tuple[PackScan, str]] = {s.pack: (s, name) for s, name in scans}
    children: Dict[str, List[str]] = {p: [] for p in by_pack}
    roots: List[str] = []
    for scan, _name in scans:
        parent_pack = id_to_pack.get(scan.root_parentid) if scan.root_parentid else None
        if parent_pack and parent_pack in by_pack and parent_pack != scan.pack:
            children[parent_pack].append(scan.pack)
        else:
            roots.append(scan.pack)

    def sort_key(pack: str):
        scan = by_pack[pack][0]
        return (scan.root_tocorder, scan.root_title.lower())

    lines = [
        "# TIA Portal Information System — Index",
        "",
        "Generated Markdown port of the Siemens TIA Portal offline help. Each entry",
        "is one content pack; nesting follows the help's own table-of-contents tree.",
        "",
    ]

    seen: set = set()

    def emit(pack: str, depth: int) -> None:
        if pack in seen:  # guard against cycles
            return
        seen.add(pack)
        scan, name = by_pack[pack]
        indent = "  " * depth
        suffix = f" — {len(scan.order)} topics" if scan.order else ""
        lines.append(f"{indent}- [{scan.root_title}]({quote(name)}.md){suffix}")
        for child in sorted(children.get(pack, []), key=sort_key):
            emit(child, depth + 1)

    for pack in sorted(roots, key=sort_key):
        emit(pack, 0)

    # Any packs not reached (shouldn't happen) are appended flat.
    for scan, name in scans:
        if scan.pack not in seen:
            lines.append(f"- [{scan.root_title}]({quote(name)}.md)")

    path = os.path.join(out_dir, "INDEX.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


def convert_corpus(
    root: str, out_dir: str, *, progress=None, keep_images: bool = True, resume: bool = False
) -> dict:
    """Convert every pack under ``root`` into ``out_dir`` with cross-pack links + INDEX.md.

    With ``keep_images=False`` the diagrams are not copied (handy when the
    Markdown is committed to git but the images are not). With ``resume=True`` an
    interrupted run picks up where it left off, reusing packs already written
    (tracked in a ``.siemens_checkpoint.json`` in the output directory)."""
    sources = discover_packs(root)
    if not sources:
        raise ValueError(f"no content packs (.zip or extracted folders) found in {root}")
    os.makedirs(out_dir, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="siemens_corpus_") as tmp:
        # Pass 1 — scan every pack, assign section names, build the global map.
        scans: List[Tuple[PackScan, str]] = []
        used_lower: set = set()
        id_to_target: Dict[str, Tuple[str, str]] = {}
        id_to_pack: Dict[str, str] = {}
        for src in sources:
            pack_dir = src
            if os.path.isfile(src):
                pack_dir = os.path.join(tmp, os.path.splitext(os.path.basename(src))[0])
                _extract.extract_pack(src, pack_dir)
            try:
                scan = scan_pack(pack_dir)
            except ValueError:
                continue  # skip packs without a usable TOC
            name = _unique_name(_safe_filename(scan.root_title), scan.pack, used_lower)
            used_lower.add(name.lower())
            scans.append((scan, name))
            for itemid, anchor in scan.id_to_anchor.items():
                id_to_target[itemid] = (name, anchor)
                id_to_pack[itemid] = scan.pack

        # Pass 2 — render each pack with the global resolver. A failure on one
        # pack is isolated (recorded and skipped) so it can't abort the run, and
        # a checkpoint after each pack lets an interrupted run resume.
        done = _load_checkpoint(out_dir) if resume else set()
        results = []
        failures = []
        for i, (scan, name) in enumerate(scans, 1):
            md_path = os.path.join(out_dir, f"{name}.md")
            if resume and scan.pack in done and os.path.exists(md_path):
                if progress:
                    progress(i, len(scans), f"{name} (cached)")
                continue
            try:
                resolve = make_corpus_resolver(scan.file_to_anchor, id_to_target)
                markdown, images_used, missing = render_section(scan, resolve)
                with open(md_path, "w", encoding="utf-8") as fh:
                    fh.write(markdown)
                if keep_images:
                    copy_images(images_used, _extract.find_layout(scan.pack_dir).images_dir, out_dir)
                results.append({"pack": scan.pack, "name": name, "topics": len(scan.order), "missing": missing})
                done.add(scan.pack)
                _save_checkpoint(out_dir, done)
            except Exception as exc:  # noqa: BLE001 - keep the batch going
                failures.append({"pack": scan.pack, "name": name, "error": f"{type(exc).__name__}: {exc}"})
            if progress:
                progress(i, len(scans), name)

        index_path = _write_index(out_dir, scans, id_to_pack)

    return {
        "packs": len(scans),
        "converted": len(results),
        "failures": failures,
        "index": index_path,
        "out_dir": out_dir,
        "results": results,
    }
