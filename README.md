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

In **corpus mode** (converting a whole folder of packs at once), cross-**pack**
links (`../../OtherPack/…`) are rewritten to the target section file and heading
(`Other Section.md#anchor`), and an `INDEX.md` is generated from the help's own
table-of-contents tree. Converting a single pack on its own leaves cross-pack
links as plain text (there is nothing to point them at).

## Install

Requires Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Use

**Whole offline help** (recommended) — point it at the unzipped `en-US/` folder
(a folder of pack `.zip`s and/or extracted pack folders):

```bash
python -m siemenshelp path/to/en-US/ -o markdown_out/
```

This converts every pack, rewrites cross-pack links between them, collects all
diagrams under `markdown_out/images/`, and writes a top-level `markdown_out/INDEX.md`
that mirrors the help's table-of-contents tree.

**One pack** (a `.zip` or an already-extracted folder):

```bash
python -m siemenshelp path/to/TFPIDMainenUS.zip -o output/
# -> output/PID control.md  (+ output/images/)
```

### From Python

```python
from siemenshelp import convert_pack, convert_corpus

# one pack
result = convert_pack("TFPIDMainenUS.zip", "output/")

# a whole folder of packs (cross-pack links + INDEX.md)
summary = convert_corpus("path/to/en-US/", "markdown_out/")
print(summary["packs"], "packs ->", summary["index"])
```

## Publishing the generated corpus

The generated Markdown is meant to live in this repo (under `help/`) as a
reference Claude Code can grep. The **image folder is deliberately not committed**
— it is large and Claude reads the `alt` text, not the PNG — so `.gitignore`
excludes `help/images/`.

Run the full conversion into `help/` and commit just the Markdown:

```bash
python -m siemenshelp path/to/en-US/ -o help/ --no-images
git add help/                    # .gitignore keeps help/images/ out
git commit -m "Add generated Markdown corpus"
git push
```

`--no-images` skips copying the diagrams entirely (fastest, smallest). Drop the
flag if you also want the images on disk for local browsing — they still won't be
committed, because `help/images/` is git-ignored.

## Examples

`examples/` is a corpus run over three interlinked packs — note `INDEX.md` and
the resolved cross-pack link from PID into *Configuring a software controller*:

- `examples/INDEX.md` — generated table-of-contents tree
- `examples/PID control.md` — `TFPIDMainenUS` (19 topics, technology function)
- `examples/Configuring a software controller.md` — `TFTOPIDSWenUS` (37 topics)
- `examples/SINAMICS S-G infeed units.md` — `Stdr010000UIenUS` (27 topics, drive UI)

## Project layout

```
siemenshelp/
├── extract.py    unzip a pack (Windows backslash-safe); locate its parts
├── topic.py      parse one .htm: Siemens meta + <div id="nstext">
├── html2md.py    Siemens-aware HTML -> Markdown (tables, notes, images, sub/sup)
├── toc.py        parse Toc/Default.xml into an ordered topic tree
├── links.py      GitHub-style anchor slugs + cross-reference resolution
├── assemble.py   scan a pack + render its topics into one section .md
├── corpus.py     whole-folder conversion: cross-pack links + INDEX.md
└── convert.py    convert a pack or a folder of packs + CLI
```

## Status / roadmap

- **Phase 1 (done)** — per-pack converter, validated on PID and SINAMICS packs.
- **Phase 2 (done)** — cross-pack link rewriting + a global `INDEX.md` built from
  the help's ~800-pack table-of-contents tree (see `corpus.py`).
- **Phase 3** — resume-capable batch runner (checkpointing) for very large runs.
- **Phase 4** — QA sweep (broken links, empty topics), packaging.
