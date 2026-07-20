"""Convert a topic's ``<div id="nstext">`` content to Markdown.

The topic HTML uses Siemens-specific conventions that a generic HTML→Markdown
pass would mangle, so the tree is normalised first and then rendered with
:mod:`markdownify`:

* ``<p class="Blocktitle"/"BlocktitleFirst">`` are in-topic sub-headings → ``<hN>``.
* Content images (``../images/x.png?culture=en-US``) → ``images/x.png``; decorative
  Branding icons and ``missing_image`` placeholders are dropped.
* Table cells wrap text in ``<p class="p_table_*">``; these are flattened to
  inline content (multi-paragraph cells joined with ``<br>``) so GitHub-flavoured
  Markdown tables render correctly.
* ``<sub>``/``<sup>`` (units like Tᵤ, vₘₐₓ) are preserved as HTML so the
  distinction survives.
* Stray ``<a id="…"/>`` anchors are removed; ``ContentNode`` links are rewritten
  via the supplied resolver (unresolved ones render as plain text).
"""
from __future__ import annotations

import re
import warnings
from typing import Callable, Optional, Set

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from markdownify import MarkdownConverter

# The topic files are XHTML; parsing them with the (lenient) lxml HTML parser
# works well but makes bs4 emit this advisory warning. Silence it.
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

_HEADING_RE = re.compile(r"^h[1-6]$")
_QUERY_RE = re.compile(r"\?.*$")
_BLANKS_RE = re.compile(r"\n{3,}")


class _SiemensConverter(MarkdownConverter):
    """markdownify tuned for technical reference text (keep sub/sup, no escaping)."""

    def convert_sub(self, el, text, parent_tags):
        return f"<sub>{text}</sub>" if text else ""

    def convert_sup(self, el, text, parent_tags):
        return f"<sup>{text}</sup>" if text else ""

    def escape(self, text, parent_tags=None):
        """Escape HTML-significant characters in body text.

        The help is full of literal angle brackets — placeholders like
        ``<Project ID>`` and comparison operators like ``< 0.1`` — which a
        Markdown renderer would otherwise swallow as HTML tags. We entity-escape
        ``&``, ``<`` and ``>`` (but not inside code, which markdownify handles
        separately) while leaving other punctuation alone, so ordinary technical
        prose stays clean (no backslash noise)."""
        if not text:
            return text
        text = super().escape(text, parent_tags)
        if parent_tags and ("code" in parent_tags or "pre" in parent_tags):
            return text
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _img_basename(src: str) -> str:
    return _QUERY_RE.sub("", src or "").rsplit("/", 1)[-1]


# Single-column tables are layout wrappers, not data: Note/Warning callout boxes
# and step-list boxes. They read far better as blockquotes / ordered lists.
_NOTE_CLASSES = (
    "safety", "warning", "note", "caution", "hint", "important", "attention", "danger", "notice",
)
_NOTE_WORDS = {"note", "notice", "warning", "caution", "danger", "attention", "important"}


def _looks_like_note(table) -> bool:
    classes = " ".join(table.get("class", []) or []).lower()
    if any(k in classes for k in _NOTE_CLASSES):
        return True
    lead = table.find(["b", "strong", "p"])
    if lead and lead.get_text(strip=True).rstrip(":").lower() in _NOTE_WORDS:
        return True
    return False


def _unwrap_single_col_table(soup: BeautifulSoup, table) -> None:
    """Replace a one-column layout table with its content: a blockquote for
    Note/Warning boxes, otherwise the cell's blocks spliced in place (so step
    lists become real ordered lists)."""
    note = _looks_like_note(table)
    wrapper = soup.new_tag("blockquote") if note else soup.new_tag("div")
    for cell in table.find_all(["td", "th"]):
        for child in list(cell.contents):
            wrapper.append(child.extract())
    table.replace_with(wrapper)
    if not note:
        wrapper.unwrap()


def _normalize_tables(soup: BeautifulSoup, container) -> None:
    """Make every table rectangular with a header row so it renders as valid GFM.

    Siemens tables use ``colspan`` for full-width note rows and an empty
    ``<thead/>`` for legend/key tables. Both break pipe tables, so we expand
    colspans into empty filler cells, pad short rows, and synthesise a blank
    header when the table has no real header cells.
    """
    for table in container.find_all("table"):
        # <colgroup>/<col> carry only width hints and make markdownify emit
        # stray blank lines between the header and body (splitting the table).
        for col in table.find_all(["colgroup", "col"]):
            col.decompose()
        rows = table.find_all("tr")
        if not rows:
            continue
        cols = max(
            sum(int(c.get("colspan", 1) or 1) for c in tr.find_all(["td", "th"], recursive=False))
            for tr in rows
        )
        if not cols:
            continue
        if cols == 1:
            _unwrap_single_col_table(soup, table)
            continue
        for tr in rows:
            for cell in tr.find_all(["td", "th"], recursive=False):
                span = int(cell.get("colspan", 1) or 1)
                if span > 1:
                    del cell["colspan"]
                    ref = cell
                    for _ in range(span - 1):
                        filler = soup.new_tag(cell.name)
                        ref.insert_after(filler)
                        ref = filler
            have = len(tr.find_all(["td", "th"], recursive=False))
            for _ in range(cols - have):
                tr.append(soup.new_tag("td"))

        thead = table.find("thead")
        if not (thead and thead.find(["th", "td"])):
            if thead:
                thead.decompose()
            # Header-less tables are almost always symbol/description legends;
            # give the common two-column case a readable generic header.
            labels = ["Symbol", "Meaning"] if cols == 2 else [""] * cols
            new_thead = soup.new_tag("thead")
            header_row = soup.new_tag("tr")
            for label in labels:
                th = soup.new_tag("th")
                if label:
                    th.string = label
                header_row.append(th)
            new_thead.append(header_row)
            table.insert(0, new_thead)


def _preprocess(
    soup: BeautifulSoup,
    container,
    *,
    sub_level: int,
    images_used: Set[str],
    resolve_link: Callable[[Optional[str]], Optional[str]],
) -> None:
    # Drop scripts/styles outright.
    for tag in container.find_all(["script", "style"]):
        tag.decompose()

    # Block titles -> headings (one level below the topic's own heading);
    # note/warning sub-headings -> bold so they stay visually distinct.
    for p in container.find_all("p"):
        classes = " ".join(p.get("class", []) or [])
        if "Blocktitle" in classes:  # matches Blocktitle and BlocktitleFirst
            p.name = f"h{sub_level}"
            p.attrs = {}
        elif "subheading" in classes:
            strong = soup.new_tag("strong")
            for child in list(p.contents):
                strong.append(child.extract())
            p.append(strong)
            p.attrs = {}

    # Images: keep content diagrams, drop decorative icons/placeholders.
    for img in list(container.find_all("img")):
        src = img.get("src", "") or ""
        if "Branding/" in src or "missing_image" in src:
            img.decompose()
            continue
        base = _img_basename(src)
        if not base:
            img.decompose()
            continue
        images_used.add(base)
        img["src"] = f"images/{base}"
        alt = (img.get("alt") or "").strip()
        if not alt:
            heading = img.find_previous(_HEADING_RE)
            alt = heading.get_text(strip=True) if heading else "Figure"
        img.attrs = {"src": f"images/{base}", "alt": alt}

    # Links: rewrite or flatten to text.
    for a in list(container.find_all("a")):
        href = a.get("href")
        if not href:
            a.unwrap() if a.contents else a.decompose()
            continue
        target = resolve_link(href)
        if target:
            a.attrs = {"href": target}
        else:
            a.unwrap()

    # Make tables rectangular and header-bearing before flattening cells.
    _normalize_tables(soup, container)

    # Table cells: flatten <p>/<div> wrappers to inline text, joining multiple
    # blocks with <br> so the cell stays on one Markdown table row.
    for cell in container.find_all(["td", "th"]):
        blocks = cell.find_all(["p", "div"], recursive=False)
        for i, block in enumerate(blocks):
            if i:
                block.insert_before(soup.new_tag("br"))
        for block in list(cell.find_all(["p", "div"])):
            block.unwrap()

    # Remove now-empty paragraphs (avoids runs of blank lines).
    for p in list(container.find_all("p")):
        if not p.get_text(strip=True) and not p.find("img"):
            p.decompose()


def to_markdown(
    nstext,
    *,
    base_level: int,
    images_used: Set[str],
    resolve_link: Callable[[Optional[str]], Optional[str]],
) -> str:
    """Render one topic body to Markdown. ``base_level`` is the topic's own
    heading level; in-topic block titles are emitted one level deeper."""
    if nstext is None:
        return ""

    # Work on an isolated copy so the source tree is never mutated.
    soup = BeautifulSoup(str(nstext), "lxml")
    container = soup.find(id="nstext") or soup.body or soup
    _preprocess(
        soup,
        container,
        sub_level=min(base_level + 1, 6),
        images_used=images_used,
        resolve_link=resolve_link,
    )

    converter = _SiemensConverter(
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        escape_misc=False,
        table_infer_header=True,
        newline_style="spaces",
        strip=["script", "style"],
        # Keep content diagrams that sit inside cells/paragraphs/links, which
        # markdownify would otherwise reduce to bare alt text.
        keep_inline_images_in=["td", "th", "p", "div", "span", "li", "a", "figure"],
    )
    md = converter.convert_soup(container)
    return _BLANKS_RE.sub("\n\n", md).strip()
