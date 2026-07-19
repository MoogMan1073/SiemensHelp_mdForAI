"""Assemble one content pack into a single Markdown *section* file.

The pack's topics are emitted in table-of-contents order, each under a heading
whose level matches its TOC depth (root = ``#``). In-topic block titles nest one
level deeper. YAML front-matter records the pack, title, topic count and the
devices the pack applies to. Content images are copied into ``output/images/``.
"""
from __future__ import annotations

import os
import shutil
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple

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


def _front_matter(title: str, pack: str, topics: int, devices: List[str]) -> str:
    lines = [
        "---",
        f'title: "{title}"',
        f"package: {pack}",
        f"topics: {topics}",
    ]
    if devices:
        lines.append(f"devices: [{', '.join(devices)}]")
    lines += [
        "source: Siemens TIA Portal Information System (offline help, en-US)",
        "---",
        "",
    ]
    return "\n".join(lines)


def assemble_pack(pack_dir: str, out_dir: str, *, section_name: Optional[str] = None) -> dict:
    """Convert an extracted pack folder to ``<section>.md`` in ``out_dir``."""
    layout = _extract.find_layout(pack_dir)
    if not layout.toc_path:
        raise ValueError(f"no Toc/Default.xml found in {pack_dir}")

    root = parse_toc(layout.toc_path)
    order: List[Tuple[TocNode, int]] = flatten(root) if root else []
    if not order:
        raise ValueError(f"empty table of contents in {pack_dir}")

    pack = order[0][0].pack or os.path.basename(pack_dir.rstrip("/"))
    root_title = order[0][0].title or pack
    devices = _parse_devices(layout.scope_path)

    # First pass: assign a collision-free anchor to every topic so same-pack
    # cross-links can target the exact rendered heading anchor.
    slug = uniq_slugger()
    file_to_anchor: Dict[str, str] = {}
    anchored: List[Tuple[TocNode, int, str]] = []
    for node, depth in order:
        anchor = slug(node.title)
        anchored.append((node, depth, anchor))
        file_to_anchor.setdefault(node.topic_file, anchor)
    resolve = make_resolver(file_to_anchor)

    # Second pass: render each topic body.
    images_used: set = set()
    parts: List[str] = [_front_matter(root_title, pack, len(order), devices)]
    missing = 0
    for node, depth, _anchor in anchored:
        level = min(depth + 1, 6)
        heading = f"{'#' * level} {node.title}".rstrip()
        topic_path = os.path.join(pack_dir, *node.rel_path.split("/"))
        body = ""
        if os.path.exists(topic_path):
            topic = parse_topic(topic_path)
            body = to_markdown(
                topic.nstext,
                base_level=level,
                images_used=images_used,
                resolve_link=resolve,
            )
        else:
            missing += 1
        parts.append(heading + (f"\n\n{body}" if body else ""))

    markdown = "\n\n".join(parts).rstrip() + "\n"

    os.makedirs(out_dir, exist_ok=True)
    name = section_name or _safe_filename(root_title) or pack
    md_path = os.path.join(out_dir, f"{name}.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)

    copied = _copy_images(images_used, layout.images_dir, out_dir)

    return {
        "pack": pack,
        "title": root_title,
        "md_path": md_path,
        "topics": len(order),
        "images": copied,
        "images_referenced": len(images_used),
        "missing": missing,
        "devices": devices,
    }


def _copy_images(names: set, images_dir: Optional[str], out_dir: str) -> int:
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
