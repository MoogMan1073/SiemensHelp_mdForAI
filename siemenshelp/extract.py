"""Unzip a content pack and locate its parts.

Content-pack zips are produced on Windows, so their member names use
backslashes as path separators (``17007794059\\17007794059.htm``). Python's
:mod:`zipfile` treats a backslash as an ordinary character, which on Linux/macOS
would create a single file literally named ``a\\b.htm`` instead of a nested
folder. :func:`extract_pack` normalises separators (and guards against path
traversal) so the pack extracts the same way on every platform.
"""
from __future__ import annotations

import os
import zipfile
from dataclasses import dataclass

# Directories that are structural, not topic folders.
SPECIAL_DIRS = {"images", "Toc", "Scope"}


def _norm_members(zf: zipfile.ZipFile):
    """Yield ``(ZipInfo, relative_posix_path)`` with separators normalised."""
    for info in zf.infolist():
        name = info.filename.replace("\\", "/")
        parts = [p for p in name.split("/") if p not in ("", ".", "..")]
        if not parts:
            continue
        yield info, "/".join(parts)


def extract_pack(zip_path: str, dest_dir: str) -> str:
    """Extract ``zip_path`` into ``dest_dir``; return ``dest_dir``."""
    os.makedirs(dest_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        for info, rel in _norm_members(zf):
            target = os.path.join(dest_dir, *rel.split("/"))
            if info.is_dir() or info.filename.endswith(("/", "\\")):
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target) or dest_dir, exist_ok=True)
            with zf.open(info) as src, open(target, "wb") as out:
                out.write(src.read())
    return dest_dir


@dataclass
class PackLayout:
    """Where a pack's parts live on disk (topic files are resolved via the TOC)."""

    root: str
    images_dir: str | None
    toc_path: str | None
    scope_path: str | None


def find_layout(pack_dir: str) -> PackLayout:
    """Locate ``images/``, ``Toc/Default.xml`` and ``Scope/HelpScope.xml``."""
    entries = set(os.listdir(pack_dir)) if os.path.isdir(pack_dir) else set()
    images_dir = os.path.join(pack_dir, "images")
    toc_path = os.path.join(pack_dir, "Toc", "Default.xml")
    scope_path = os.path.join(pack_dir, "Scope", "HelpScope.xml")
    return PackLayout(
        root=pack_dir,
        images_dir=images_dir if "images" in entries else None,
        toc_path=toc_path if os.path.exists(toc_path) else None,
        scope_path=scope_path if os.path.exists(scope_path) else None,
    )
