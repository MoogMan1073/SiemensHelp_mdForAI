# SiemensHelp_mdForAI

Convert the **Siemens TIA Portal Information System** offline help into clean,
navigable **Markdown** — a grep-friendly reference source for Claude Code (and
any other tool or human that would rather read Markdown than click through
compiled HTML help).

The offline help ships as `en-US.zip` (~486 MB). Unzipped, it is **~800
"content-pack" zips**, one per product/topic area (e.g. `TFPIDMainenUS.zip` for
PID control, `StdrS120ConfenUS.zip` for SINAMICS S120), plus an
`InstallationInfo.xml` manifest and shared `Branding/`, `Synonyms/` folders.

This tool turns **one content pack into one self-contained Markdown section
file**: the pack's topics, concatenated in table-of-contents order, with nested
headings, preserved tables, linked diagrams and rewritten cross-references.

```
TFPIDMainenUS.zip   ─►   PID control.md   +   images/
```

## What's in a content pack

Each pack unzips to:

```
<rootTopicId>/         numeric-id .htm topic files (self-describing XHTML)
images/                PNG diagrams
Toc/Default.xml        topic hierarchy + human titles + order
Scope/HelpScope.xml    device applicability (S7-1200 / S7-1500 / ...)
```

Every `.htm` carries `Siemens.TIAHelp.*` `<meta>` tags (title, parent, order,
category, scope) and puts its visible content in `<div id="nstext">`. Because a
topic's `TocParentId` can point into *another* pack, all ~800 packs form one
global tree — which a later pass uses to build a cross-linked index.

## What the converter does

- **Concatenates** a pack's topics in TOC order, one Markdown file per pack.
- **Headings** follow the TOC depth; in-topic block titles nest one level below.
- **Tables** are made valid GitHub-flavoured Markdown (colspans expanded, ragged
  rows padded, a header row ensured, width-only `<colgroup>` stripped).
- **Note / Warning callout boxes** (single-cell `class="safety"` tables) become
  blockquotes; **step boxes** (`<ol class="action">`) become ordered lists.
- **Images** are copied to `images/` and linked; decorative Branding icons and
  `missing_image` placeholders are dropped; empty `alt` is filled from the
  nearest heading.
- **Cross-references** within a pack are rewritten to `#anchor` fragments;
  `<sub>`/`<sup>` (units such as Tᵤ, vₘₐₓ) are preserved.
- **Front-matter** records the package, title, topic count and applicable devices.
- Chrome (the `nsbanner` title bar, stylesheet/script links) is discarded.

> Cross-**pack** links (`../../OtherPack/…`) can't be resolved from a single
> pack, so for now they render as plain text; the global index + cross-pack link
> rewriting is the next phase.

## Install

Requires Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Use

Convert one pack (a `.zip` or an already-extracted folder):

```bash
python -m siemenshelp path/to/TFPIDMainenUS.zip -o output/
# -> output/PID control.md  (+ output/images/)
```

Convert the whole offline help — point it at every pack. On macOS/Linux:

```bash
mkdir -p markdown_out
for z in path/to/en-US/*.zip; do
    python -m siemenshelp "$z" -o markdown_out/
done
```

Each pack becomes `markdown_out/<Section title>.md`, with all diagrams collected
under `markdown_out/images/`.

### From Python

```python
from siemenshelp import convert_pack

result = convert_pack("TFPIDMainenUS.zip", "output/")
print(result["md_path"], result["topics"], "topics", result["images"], "images")
```

## Examples

`examples/` holds validated output from two different product families:

- `examples/PID control.md` — from `TFPIDMainenUS` (19 topics, technology function)
- `examples/SINAMICS S-G infeed units.md` — from `Stdr010000UIenUS` (27 topics, drive UI)

## Project layout

```
siemenshelp/
├── extract.py    unzip a pack (Windows backslash-safe); locate its parts
├── topic.py      parse one .htm: Siemens meta + <div id="nstext">
├── html2md.py    Siemens-aware HTML -> Markdown (tables, notes, images, sub/sup)
├── toc.py        parse Toc/Default.xml into an ordered topic tree
├── links.py      GitHub-style anchor slugs + cross-reference resolution
├── assemble.py   concatenate a pack's topics into one section .md
└── convert.py    convert a pack (zip or folder) + CLI
```

## Status / roadmap

- **Phase 1 (done)** — per-pack converter, validated on PID and SINAMICS packs.
- **Phase 2** — cross-pack link rewriting + a global `INDEX.md` from the ~800-pack tree.
- **Phase 3** — resume-capable batch runner over the whole `en-US/` folder.
- **Phase 4** — QA sweep (broken links, empty topics), packaging.
