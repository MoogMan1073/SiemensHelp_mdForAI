"""End-to-end test for whole-corpus conversion (cross-pack links + INDEX)."""
import os

import pytest

pytest.importorskip("bs4")
pytest.importorskip("markdownify")

from siemenshelp.corpus import convert_corpus  # noqa: E402

_TOC = """<?xml version="1.0" encoding="utf-8"?>
<Toc xmlns="http://www.siemens.com/2014/09/Automation/HelpPrototype/TocStorage">
  <TocEntry itemid="{itemid}" title="{title}" tocorder="100" isdefault="true"{parent} />
</Toc>
"""

_HTM = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta name="Siemens.TIAHelp.Id" content="{itemid}" />
<meta name="Siemens.TIAHelp.TocTitle" content="{title}" />
<title>{title}</title></head>
<body><div id="nstext">{body}</div></body></html>
"""


def _make_pack(root, pack, folder, topic, title, body, parentid=None):
    pack_dir = os.path.join(root, pack)
    os.makedirs(os.path.join(pack_dir, folder))
    os.makedirs(os.path.join(pack_dir, "Toc"))
    itemid = f"{pack}/{folder}/{topic}"
    parent = f' parentid="{parentid}"' if parentid else ""
    with open(os.path.join(pack_dir, "Toc", "Default.xml"), "w", encoding="utf-8") as fh:
        fh.write(_TOC.format(itemid=itemid, title=title, parent=parent))
    with open(os.path.join(pack_dir, folder, topic), "w", encoding="utf-8") as fh:
        fh.write(_HTM.format(itemid=itemid, title=title, body=body))


def test_convert_corpus_cross_pack_links_and_index(tmp_path):
    root = tmp_path / "packs"
    out = tmp_path / "out"
    root.mkdir()

    # Alpha links (in its body) to Beta; Beta's TOC parent is Alpha's root.
    _make_pack(
        str(root), "PA", "1", "1.htm", "Alpha",
        '<p>See <a class="ContentNode" href="../../PB/2/2.htm">Beta</a>.</p>',
    )
    _make_pack(
        str(root), "PB", "2", "2.htm", "Beta",
        "<p>Beta content.</p>",
        parentid="PA/1/1.htm",
    )

    result = convert_corpus(str(root), str(out))
    assert result["packs"] == 2

    alpha = (out / "Alpha.md").read_text()
    # cross-pack link resolved to the target section file + heading anchor
    assert "[Beta](Beta.md#beta)" in alpha

    index = (out / "INDEX.md").read_text()
    # Beta nests under Alpha (its TOC parent), so it is the more-indented entry
    assert "- [Alpha](Alpha.md)" in index
    assert "  - [Beta](Beta.md)" in index


def test_case_insensitive_filename_dedup(tmp_path):
    root = tmp_path / "packs"
    out = tmp_path / "out"
    root.mkdir()
    # Two packs whose titles differ only in case must not collide to one file.
    _make_pack(str(root), "PA", "1", "1.htm", "Widget", "<p>a</p>")
    _make_pack(str(root), "PB", "2", "2.htm", "widget", "<p>b</p>")
    convert_corpus(str(root), str(out))
    mds = [f.name for f in out.glob("*.md") if f.name != "INDEX.md"]
    assert len(mds) == 2
    assert len({m.lower() for m in mds}) == 2  # distinct even case-insensitively


def test_resume_skips_completed(tmp_path):
    root = tmp_path / "packs"
    out = tmp_path / "out"
    root.mkdir()
    _make_pack(str(root), "PA", "1", "1.htm", "Alpha", "<p>a</p>")
    first = convert_corpus(str(root), str(out), resume=True)
    assert first["converted"] == 1
    second = convert_corpus(str(root), str(out), resume=True)
    assert second["converted"] == 0  # reused from the checkpoint


def test_empty_title_becomes_untitled(tmp_path):
    root = tmp_path / "packs"
    out = tmp_path / "out"
    root.mkdir()
    _make_pack(str(root), "PA", "1", "1.htm", "", "<p>body</p>")
    convert_corpus(str(root), str(out))
    txt = (out / "PA.md").read_text()
    assert "(untitled)" in txt
    assert not any(line.rstrip() in ("#", "##", "###") for line in txt.splitlines())
