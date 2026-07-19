"""Tests for TOC parsing/flattening (uses only the stdlib XML parser)."""
import os
import tempfile

from siemenshelp.toc import flatten, parse_toc

_TOC = """<?xml version="1.0" encoding="utf-8"?>
<Toc xmlns="http://www.siemens.com/2014/09/Automation/HelpPrototype/TocStorage">
  <TocEntry itemid="P/1/root.htm" title="Root" tocorder="200" isdefault="true">
    <TocEntry itemid="P/1/b.htm" title="Second" tocorder="200" parentid="P/1/root.htm" />
    <TocEntry itemid="P/1/a.htm" title="First" tocorder="100" parentid="P/1/root.htm">
      <TocEntry itemid="P/1/a1.htm" title="Deep" tocorder="100" parentid="P/1/a.htm" />
    </TocEntry>
  </TocEntry>
</Toc>
"""


def _write(text):
    fd, path = tempfile.mkstemp(suffix=".xml")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def test_parse_and_flatten_order_and_depth():
    path = _write(_TOC)
    try:
        root = parse_toc(path)
    finally:
        os.remove(path)

    assert root is not None
    assert root.title == "Root"
    assert root.pack == "P"
    assert root.rel_path == "1/root.htm"
    assert root.topic_file == "root.htm"

    order = flatten(root)
    # tocorder puts "First" (100) before "Second" (200); "Deep" nests under First.
    titles = [n.title for n, _ in order]
    depths = [d for _, d in order]
    assert titles == ["Root", "First", "Deep", "Second"]
    assert depths == [0, 1, 2, 1]
