"""Convert the Siemens TIA Portal Information System offline help to Markdown.

The offline help (``en-US.zip``) is a collection of ~800 *content-pack* zips,
one per product/topic area (e.g. ``TFPIDMainenUS.zip`` for PID control). Each
pack contains numeric-id ``.htm`` topic files, an ``images/`` folder, a
``Toc/Default.xml`` (topic hierarchy + human titles) and a ``Scope/HelpScope.xml``
(device applicability).

This package turns one pack into a single, self-contained Markdown *section*
file: the pack's topics concatenated in table-of-contents order, with nested
headings, preserved tables, linked images and rewritten cross-references.

Entry points:

* :func:`siemenshelp.convert.convert_pack` — convert one pack (zip or folder).
* ``python -m siemenshelp <pack.zip> -o output/`` — the CLI.
"""
from __future__ import annotations

from .convert import convert_pack
from .corpus import convert_corpus

__all__ = ["convert_pack", "convert_corpus"]
__version__ = "0.2.0"
