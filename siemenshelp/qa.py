"""Lint a generated Markdown corpus.

Checks a converted output directory for the problems that matter in a reference
corpus: broken intra-document anchors, broken cross-file links, leftover HTML
tags or help chrome, malformed tables, empty headings and INDEX coverage.

Run it after a conversion to confirm the output is clean:

    python -m siemenshelp.qa markdown_out/

Exits non-zero if any issue is found, so it can gate a CI check.
"""
from __future__ import annotations

import glob
import os
import re
from collections import Counter
from typing import Dict, List
from urllib.parse import unquote

from .links import uniq_slugger

_HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.M)
_EMPTY_HEADING = re.compile(r"^#{1,6}[ \t]*$", re.M)
_CODE_FENCE = re.compile(r"```.*?```", re.S)
_CODE_SPAN = re.compile(r"`[^`]*`")
_TAG = re.compile(r"</?([a-zA-Z][a-zA-Z0-9]*)")
_INTRA_LINK = re.compile(r"\]\(#([^)]+)\)")
_FILE_LINK = re.compile(r"\]\(([^)#][^)#]*)\.md#([^)]+)\)")
_INDEX_LINK = re.compile(r"\]\(([^)#]+)\.md\)")
_REL_UP = re.compile(r"\]\(\.\./")
# A separator row (contains a real '---') divorced from its body by a blank line.
_TABLE_SPLIT = re.compile(r"^\|[\s|:]*-[-\s|:]*\|[ \t]*\n[ \t]*\n\|", re.M)

_KNOWN_TAGS = {"sub", "sup", "br"}


def _anchors(md: str) -> set:
    """Reproduce the heading anchors the generator would have produced."""
    slug = uniq_slugger()
    return {slug(m.group(1)) for m in _HEADING.finditer(md)}


def _strip_code(md: str) -> str:
    return _CODE_SPAN.sub("", _CODE_FENCE.sub("", md))


def lint_corpus(out_dir: str) -> dict:
    files = sorted(glob.glob(os.path.join(out_dir, "*.md")))
    texts = {os.path.basename(f): open(f, encoding="utf-8").read() for f in files}
    anchors = {name: _anchors(md) for name, md in texts.items()}
    names = set(anchors)

    issues: Counter = Counter()
    examples: Dict[str, List[str]] = {}

    def flag(kind: str, example: str) -> None:
        issues[kind] += 1
        examples.setdefault(kind, [])
        if len(examples[kind]) < 5:
            examples[kind].append(example)

    index_targets: set = set()

    for name, md in texts.items():
        for a in _INTRA_LINK.findall(md):
            if a not in anchors[name]:
                flag("broken_intra_anchor", f"{name} -> #{a}")
        for tgt, a in _FILE_LINK.findall(md):
            fn = unquote(tgt) + ".md"
            if fn not in names:
                flag("broken_link_target_missing", f"{name} -> {fn}")
            elif a not in anchors[fn]:
                flag("broken_link_anchor", f"{name} -> {fn}#{a}")
        for _ in _EMPTY_HEADING.findall(md):
            flag("empty_heading", name)
        for tag in _TAG.findall(_strip_code(md)):
            if tag.lower() not in _KNOWN_TAGS:
                flag("leftover_html_tag", f"{name}: <{tag}>")
        if "?culture" in md:
            flag("leftover_culture_query", name)
        if "Branding" in md:
            flag("leftover_branding_ref", name)
        for _ in _REL_UP.findall(md):
            flag("unresolved_relative_link", name)
        for _ in _TABLE_SPLIT.finditer(md):
            flag("table_header_body_split", name)
        if name == "INDEX.md":
            for tgt in _INDEX_LINK.findall(md):
                index_targets.add(unquote(tgt) + ".md")

    if "INDEX.md" in names:
        for name in names:
            if name != "INDEX.md" and name not in index_targets:
                flag("section_missing_from_index", name)
        for tgt in index_targets:
            if tgt not in names:
                flag("index_points_to_missing_file", tgt)

    return {"files": len(files), "issues": dict(issues), "examples": examples}


def format_report(report: dict) -> str:
    lines = [f"Corpus lint: {report['files']} Markdown files"]
    issues = report["issues"]
    if not issues:
        lines.append("  no issues found ✓")
        return "\n".join(lines)
    for kind, count in sorted(issues.items(), key=lambda kv: -kv[1]):
        lines.append(f"  {kind}: {count}")
        for ex in report["examples"].get(kind, [])[:4]:
            lines.append(f"      e.g. {ex}")
    return "\n".join(lines)


def main(argv=None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="siemenshelp.qa", description="Lint a generated Markdown corpus.")
    ap.add_argument("dir", help="corpus output directory (containing the .md files)")
    args = ap.parse_args(argv)
    report = lint_corpus(args.dir)
    print(format_report(report))
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
