"""Anchor slugs and cross-reference resolution.

Because a whole pack is concatenated into one Markdown file, a topic's headings
become GitHub-style anchors and same-pack cross-links (``ContentNode`` anchors)
are rewritten to ``#anchor`` fragments. Cross-*pack* links (``../../OtherPack/…``)
cannot be resolved from a single pack, so they are left for the global pass
(Phase 2); until then the resolver returns ``None`` and the link renders as
plain text.
"""
from __future__ import annotations

import re
from typing import Callable, Dict, Optional, Tuple
from urllib.parse import quote

_PUNCT = re.compile(r"[^\w\s-]", re.UNICODE)
_SPACES = re.compile(r"\s+")


def github_slug(text: str) -> str:
    """Approximate GitHub's heading-anchor algorithm (lower, strip punct, hyphenate)."""
    s = (text or "").strip().lower()
    s = _PUNCT.sub("", s)
    s = _SPACES.sub("-", s).strip("-")
    return s


def uniq_slugger() -> Callable[[str], str]:
    """Return a function that yields collision-free slugs the way GitHub does:
    the 2nd, 3rd, ... occurrence of a slug get ``-1``, ``-2`` suffixes."""
    counts: Dict[str, int] = {}

    def make(title: str) -> str:
        base = github_slug(title) or "section"
        n = counts.get(base, 0)
        counts[base] = n + 1
        return base if n == 0 else f"{base}-{n}"

    return make


def make_resolver(file_to_anchor: Dict[str, str]) -> Callable[[Optional[str]], Optional[str]]:
    """Build a link resolver for one pack.

    Returns ``#anchor`` for same-pack topic links, passes through external/URL
    and existing-fragment links, and returns ``None`` for cross-pack links
    (``../…``) and unknown targets so the caller can render them as text.
    """

    def resolve(href: Optional[str]) -> Optional[str]:
        if not href:
            return None
        h = href.strip()
        if not h:
            return None
        if h.startswith(("#", "http://", "https://", "mailto:")):
            return h
        if "../" in h:
            return None  # cross-pack — resolved in the global pass
        base = h.split("#", 1)[0].split("?", 1)[0].rsplit("/", 1)[-1]
        anchor = file_to_anchor.get(base)
        return f"#{anchor}" if anchor else None

    return resolve


def _href_to_itemid(href: str) -> str:
    """``../../Pack/folder/topic.htm`` -> ``Pack/folder/topic.htm``."""
    path = href.split("#", 1)[0].split("?", 1)[0]
    return "/".join(p for p in path.split("/") if p not in ("..", ".", ""))


def make_corpus_resolver(
    file_to_anchor: Dict[str, str],
    id_to_target: Dict[str, Tuple[str, str]],
) -> Callable[[Optional[str]], Optional[str]]:
    """Resolver for whole-corpus conversion.

    Same-pack links become ``#anchor``; cross-pack links (``../…``) are looked up
    in the global ``id_to_target`` (itemid -> (section_file, anchor)) and become
    ``Section%20File.md#anchor``. Unknown targets return ``None`` (render as text).
    Section-file names are percent-encoded so spaces/parentheses don't break the
    Markdown link.
    """

    def resolve(href: Optional[str]) -> Optional[str]:
        if not href:
            return None
        h = href.strip()
        if not h:
            return None
        if h.startswith(("#", "http://", "https://", "mailto:")):
            return h
        if "../" not in h:
            base = h.split("#", 1)[0].split("?", 1)[0].rsplit("/", 1)[-1]
            anchor = file_to_anchor.get(base)
            return f"#{anchor}" if anchor else None
        target = id_to_target.get(_href_to_itemid(h))
        if not target:
            return None
        section_file, anchor = target
        return f"{quote(section_file)}.md#{anchor}"

    return resolve

