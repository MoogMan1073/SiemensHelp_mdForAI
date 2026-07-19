"""Parse a pack's ``Toc/Default.xml`` into an ordered topic tree.

Each ``<TocEntry>`` carries an ``itemid`` of the form ``Pack/folder/topic.htm``,
a human ``title``, a ``tocorder`` (sibling sort key) and a ``parentid`` (which
may point into *another* pack — that is how the ~800 packs stitch into one
global tree). Within a single pack, entries are nested under the pack's root
topic, so parsing one file gives that section's full hierarchy.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

_NS = "{http://www.siemens.com/2014/09/Automation/HelpPrototype/TocStorage}"


@dataclass
class TocNode:
    itemid: str
    title: str
    tocorder: int
    parentid: Optional[str]
    image_category: Optional[str]
    scope: Optional[str]
    is_default: bool
    children: List["TocNode"] = field(default_factory=list)

    @property
    def rel_path(self) -> str:
        """Path within the pack folder: ``Pack/folder/topic.htm`` -> ``folder/topic.htm``."""
        parts = self.itemid.split("/")
        return "/".join(parts[1:]) if len(parts) > 1 else self.itemid

    @property
    def topic_file(self) -> str:
        return self.itemid.split("/")[-1]

    @property
    def pack(self) -> str:
        return self.itemid.split("/")[0] if self.itemid else ""


def _make(el: ET.Element) -> TocNode:
    def g(key: str, default: Optional[str] = None) -> Optional[str]:
        return el.get(key, default)

    return TocNode(
        itemid=g("itemid", "") or "",
        title=(g("title", "") or "").strip(),
        tocorder=int(g("tocorder", "0") or 0),
        parentid=g("parentid"),
        image_category=g("imagecategory"),
        scope=g("scope"),
        is_default=(g("isdefault", "false") or "false").lower() == "true",
    )


def parse_toc(toc_path: str) -> Optional[TocNode]:
    """Return the pack's root :class:`TocNode` (or a synthetic wrapper if several)."""
    root_el = ET.parse(toc_path).getroot()
    top = root_el.findall(f"{_NS}TocEntry")
    if not top:
        return None

    def build(el: ET.Element) -> TocNode:
        node = _make(el)
        for child in el.findall(f"{_NS}TocEntry"):
            node.children.append(build(child))
        node.children.sort(key=lambda n: n.tocorder)
        return node

    roots = sorted((build(e) for e in top), key=lambda n: n.tocorder)
    if len(roots) == 1:
        return roots[0]
    wrapper = TocNode("", "", 0, None, None, None, False, children=roots)
    return wrapper


def flatten(root: TocNode) -> List[Tuple[TocNode, int]]:
    """Depth-first ``[(node, depth)]`` in ``tocorder``. A synthetic (empty-id)
    wrapper does not consume a depth level, so real roots start at depth 0."""
    out: List[Tuple[TocNode, int]] = []

    def walk(node: TocNode, depth: int) -> None:
        if node.itemid:
            out.append((node, depth))
            child_depth = depth + 1
        else:
            child_depth = depth
        for child in node.children:
            walk(child, child_depth)

    walk(root, 0)
    return out
