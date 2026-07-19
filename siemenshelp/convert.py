"""Convert a content pack or a whole folder of packs to Markdown, and CLI."""
from __future__ import annotations

import argparse
import os
import tempfile
from typing import Optional

from . import extract as _extract
from .assemble import assemble_pack
from .corpus import convert_corpus


def _is_pack_dir(path: str) -> bool:
    return os.path.isdir(path) and os.path.exists(os.path.join(path, "Toc", "Default.xml"))


def convert_pack(source: str, out_dir: str, *, section_name: Optional[str] = None) -> dict:
    """Convert one content pack. ``source`` may be a ``.zip`` or a folder."""
    if _is_pack_dir(source):
        return assemble_pack(source, out_dir, section_name=section_name)
    with tempfile.TemporaryDirectory(prefix="siemens_pack_") as tmp:
        _extract.extract_pack(source, tmp)
        return assemble_pack(tmp, out_dir, section_name=section_name)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="siemenshelp",
        description="Convert Siemens TIA Portal help content pack(s) to Markdown.",
    )
    ap.add_argument(
        "source",
        help="a content-pack .zip, an extracted pack folder, or a folder of packs "
        "(e.g. the unzipped en-US/) for whole-corpus conversion with cross-pack links",
    )
    ap.add_argument("-o", "--out", default="output", help="output directory (default: output/)")
    ap.add_argument("--name", default=None, help="override the section file name (single pack only)")
    args = ap.parse_args(argv)

    # A directory that is not itself a pack -> corpus mode.
    if os.path.isdir(args.source) and not _is_pack_dir(args.source):
        def _progress(i, total, name):
            print(f"[{i}/{total}] {name}")

        res = convert_corpus(args.source, args.out, progress=_progress)
        print(f"[ok] {res['packs']} packs -> {args.out}  (index: {res['index']})")
        return 0

    res = convert_pack(args.source, args.out, section_name=args.name)
    extra = f"  ({res['missing']} topics missing)" if res["missing"] else ""
    print(
        f"[ok] {res['pack']}: {res['topics']} topics, {res['images']} images "
        f"-> {res['md_path']}{extra}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
