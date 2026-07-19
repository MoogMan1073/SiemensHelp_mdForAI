"""Parse one ``.htm`` topic file.

Every topic is self-describing XHTML: its ``<head>`` carries ``Siemens.TIAHelp.*``
meta tags (title, parent id, order, category, scope, ...), and the visible
content lives in ``<div id="nstext">``. Everything else (the ``nsbanner`` title
chrome, Branding stylesheet/script links) is discarded — the title comes from
the meta/TOC and is emitted as a heading by the assembler.
"""
from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from typing import Dict, Optional

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

_META_PREFIX = "Siemens.TIAHelp."


@dataclass
class Topic:
    path: str
    itemid: str
    title: str
    nstext: Optional[object]  # bs4 Tag for <div id="nstext">, or None
    meta: Dict[str, str] = field(default_factory=dict)


def _read_text(path: str) -> str:
    with open(path, "rb") as fh:
        raw = fh.read()
    # utf-8-sig transparently strips the UTF-8 BOM these files start with.
    return raw.decode("utf-8-sig", errors="replace")


def parse_topic(path: str) -> Topic:
    soup = BeautifulSoup(_read_text(path), "lxml")

    meta: Dict[str, str] = {}
    for tag in soup.find_all("meta"):
        name = tag.get("name", "") or ""
        if name.startswith(_META_PREFIX):
            meta[name[len(_META_PREFIX):]] = tag.get("content", "") or ""

    title = meta.get("TocTitle") or (soup.title.string if soup.title else "") or ""
    return Topic(
        path=path,
        itemid=meta.get("Id", ""),
        title=title.strip(),
        nstext=soup.find(id="nstext"),
        meta=meta,
    )
