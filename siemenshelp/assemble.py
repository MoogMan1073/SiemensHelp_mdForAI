"""Assemble content packs into Markdown *section* files.

A pack's topics are emitted in table-of-contents order, each under a heading
whose level matches its TOC depth (root = ``#``); in-topic block titles nest one
level deeper. YAML front-matter records the pack, title, topic count and devices.
Content images are copied into ``output/images/``.

The work is split so both single-pack and whole-corpus conversion can share it:

* :func:`scan_pack` reads a pack's TOC once and assigns every topic a
  collision-free anchor (cheap; no HTML rendering).
* :func:`render_section` renders the bodies, given a link resolver.

Single-pack conversion (:func:`assemble_pack`) uses a same-pack-only resolver;
the corpus builder swaps in a global resolver that also rewrites cross-pack links.
"""
from __future__ import annotations

import os
import shutil
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Set, Tuple

from . import extract as _extract
from .html2md import to_markdown
from .links import make_resolver, uniq_slugger
from .toc import TocNode, flatten, parse_toc
from .topic import parse_topic

# Path separators read best as hyphens (S/G -> S-G); other illegal characters
# collapse to spaces.
_SEPARATORS = "/\\"
_FORBIDDEN = '<>:"|?*'


def _safe_filename(name: str) -> str:
    chars = []
    for c in name or "":
        if c in _SEPARATORS:
            chars.append("-")
        elif c in _FORBIDDEN:
            chars.append(" ")
        else:
            chars.append(c)
    cleaned = " ".join("".join(chars).split()).strip(" .")
    return cleaned[:150]


def _parse_devices(scope_path: Optional[str]) -> List[str]:
    if not scope_path or not os.path.exists(scope_path):
        return []
    try:
        root = ET.parse(scope_path).getroot()
    except ET.ParseError:
        return []
    return sorted({d.get("name") for d in root.iter("Device") if d.get("name")})


@dataclass
class PackScan:
    """The cheap-to-compute facts about a pack (no HTML rendering yet)."""

    pack: str
    pack_dir: str
    root_title: str
    root_parentid: Optional[str]
    root_tocorder: int
    devices: List[str]
    order: List[Tuple[TocNode, int]]
    file_to_anchor: Dict[str, str] = field(default_factory=dict)
    id_to_anchor: Dict[str, str] = field(default_factory=dict)
    anchors: List[str] = field(default_factory=list)  # parallel to order


def scan_pack(pack_dir: str) -> PackScan:
    layout = _extract.find_layout(pack_dir)
    if not layout.toc_path:
        raise ValueError(f"no Toc/Default.xml found in {pack_dir}")
    root = parse_toc(layout.toc_path)
    order = flatten(root) if root else []
    if not order:
        raise ValueError(f"empty table of contents in {pack_dir}")

    root_node = order[0][0]
    slug = uniq_slugger()
    file_to_anchor: Dict[str, str] = {}
    id_to_anchor: Dict[str, str] = {}
    anchors: List[str] = []
    for node, _depth in order:
        anchor = slug(node.title)
        anchors.append(anchor)
        file_to_anchor.setdefault(node.topic_file, anchor)
        id_to_anchor[node.itemid] = anchor

    return PackScan(
        pack=root_node.pack or os.path.basename(pack_dir.rstrip("/")),
        pack_dir=pack_dir,
        root_title=root_node.title or root_node.pack,
        root_parentid=root_node.parentid,
        root_tocorder=root_node.tocorder,
        devices=_parse_devices(layout.scope_path),
        order=order,
        file_to_anchor=file_to_anchor,
        id_to_anchor=id_to_anchor,
        anchors=anchors,
    )


def _front_matter(scan: PackScan) -> str:
    lines = [
        "---",
        f'title: "{scan.root_title}"',
        f"package: {scan.pack}",
        f"topics: {len(scan.order)}",
    ]
    if scan.devices:
        lines.append(f"devices: [{', '.join(scan.devices)}]")
    lines += [
        "source: Siemens TIA Portal Information System (offline help, en-US)",
        "---",
        "",
    ]
    return "\n".join(lines)


def render_section(
    scan: PackScan,
    resolve_link: Callable[[Optional[str]], Optional[str]],
) -> Tuple[str, Set[str], int]:
    """Render a pack to ``(markdown, images_used, missing_topics)``."""
    images_used: Set[str] = set()
    parts: List[str] = [_front_matter(scan)]
    missing = 0
    for (node, depth), _anchor in zip(scan.order, scan.anchors):
        level = min(depth + 1, 6)
        heading = f"{'#' * level} {node.title}".rstrip()
        topic_path = os.path.join(scan.pack_dir, *node.rel_path.split("/"))
        body = ""
        if os.path.exists(topic_path):
            topic = parse_topic(topic_path)
            body = to_markdown(
                topic.nstext,
                base_level=level,
                images_used=images_used,
                resolve_link=resolve_link,
            )
        else:
            missing += 1
        parts.append(heading + (f"\n\n{body}" if body else ""))

    markdown = "\n\n".join(parts).rstrip() + "\n"
    return markdown, images_used, missing


def copy_images(names: Set[str], images_dir: Optional[str], out_dir: str) -> int:
    if not names or not images_dir or not os.path.isdir(images_dir):
        return 0
    dest = os.path.join(out_dir, "images")
    os.makedirs(dest, exist_ok=True)
    copied = 0
    for name in names:
        src = os.path.join(images_dir, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest, name))
            copied += 1
    return copied


def assemble_pack(pack_dir: str, out_dir: str, *, section_name: Optional[str] = None) -> dict:
    """Convert a single extracted pack folder to ``<section>.md`` in ``out_dir``.

    Same-pack cross-links become ``#anchor`` fragments; cross-pack links render
    as plain text (use the corpus builder to resolve those)."""
    scan = scan_pack(pack_dir)
    resolve = make_resolver(scan.file_to_anchor)
    markdown, images_used, missing = render_section(scan, resolve)

    os.makedirs(out_dir, exist_ok=True)
    name = section_name or _safe_filename(scan.root_title) or scan.pack
    md_path = os.path.join(out_dir, f"{name}.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)

    copied = copy_images(images_used, _extract.find_layout(pack_dir).images_dir, out_dir)
    return {
        "pack": scan.pack,
        "title": scan.root_title,
        "md_path": md_path,
        "topics": len(scan.order),
        "images": copied,
        "images_referenced": len(images_used),
        "missing": missing,
        "devices": scan.devices,
    }
