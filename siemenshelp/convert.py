"""Convert a content pack (zip or extracted folder) to a Markdown section, and CLI."""
from __future__ import annotations

import argparse
import os
import tempfile
from typing import Optional

from . import extract as _extract
from .assemble import assemble_pack


def convert_pack(source: str, out_dir: str, *, section_name: Optional[str] = None) -> dict:
    """Convert one content pack. ``source`` may be a ``.zip`` or a folder."""
    if os.path.isdir(source):
        return assemble_pack(source, out_dir, section_name=section_name)
    with tempfile.TemporaryDirectory(prefix="siemens_pack_") as tmp:
        _extract.extract_pack(source, tmp)
        return assemble_pack(tmp, out_dir, section_name=section_name)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="siemenshelp",
        description="Convert a Siemens TIA Portal help content pack to Markdown.",
    )
    ap.add_argument("source", help="a content-pack .zip or an already-extracted pack folder")
    ap.add_argument("-o", "--out", default="output", help="output directory (default: output/)")
    ap.add_argument("--name", default=None, help="override the section file name (without .md)")
    args = ap.parse_args(argv)

    res = convert_pack(args.source, args.out, section_name=args.name)
    extra = f"  ({res['missing']} topics missing)" if res["missing"] else ""
    print(
        f"[ok] {res['pack']}: {res['topics']} topics, {res['images']} images "
        f"-> {res['md_path']}{extra}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
