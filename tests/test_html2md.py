"""Tests for the Siemens-aware HTML->Markdown transforms (needs bs4 + markdownify)."""
import pytest

pytest.importorskip("bs4")
pytest.importorskip("markdownify")

from siemenshelp.html2md import to_markdown  # noqa: E402


def _md(body_html, **kw):
    html = f'<div id="nstext">{body_html}</div>'
    from bs4 import BeautifulSoup

    nstext = BeautifulSoup(html, "lxml").find(id="nstext")
    kw.setdefault("base_level", 2)
    kw.setdefault("images_used", set())
    kw.setdefault("resolve_link", lambda h: None)
    return to_markdown(nstext, **kw)


def test_blocktitle_becomes_heading():
    md = _md('<p class="BlocktitleFirst">Actuators</p><p>Text.</p>', base_level=3)
    assert "#### Actuators" in md  # base_level 3 -> block title at level 4


def test_note_box_becomes_blockquote():
    html = '<table class="safety"><tr><td><p><b>Note</b></p><p>Be careful.</p></td></tr></table>'
    md = _md(html)
    assert "> **Note**" in md
    assert "> Be careful." in md
    assert "|" not in md  # not rendered as a table


def test_step_box_becomes_ordered_list():
    html = '<table><tr><td><ol class="action"><li><p>Do A.</p></li><li><p>Do B.</p></li></ol></td></tr></table>'
    md = _md(html)
    assert "1. Do A." in md
    assert "2. Do B." in md


def test_data_table_is_valid_gfm_with_colspan_padded():
    html = (
        "<table><thead><tr><th>A</th><th>B</th></tr></thead>"
        "<tbody><tr><td>1</td><td>2</td></tr>"
        '<tr><td colspan="2">wide</td></tr></tbody></table>'
    )
    md = _md(html)
    assert "| A | B |" in md
    assert "| --- | --- |" in md
    assert "| wide |  |" in md  # colspan expanded into an empty filler cell


def test_legend_table_gets_generic_header():
    html = (
        '<table class="table_legend"><tbody>'
        "<tr><td>①</td><td>ON</td></tr>"
        "<tr><td>②</td><td>OFF</td></tr></tbody></table>"
    )
    md = _md(html)
    assert "| Symbol | Meaning |" in md
    assert "| ① | ON |" in md
    # single clean table (no blank line splitting header from body)
    assert "\n\n|" not in md.split("| Symbol", 1)[1]


def test_image_rewritten_and_collected():
    used = set()
    html = '<p class="imageclass_left"><img src="../images/pic.png?culture=en-US" alt="" /></p>'
    md = _md(html, images_used=used)
    assert "images/pic.png" in md
    assert "?culture" not in md
    assert "pic.png" in used


def test_subscript_preserved_and_crosspack_link_flattened():
    md = _md('<p>T<sub>u</sub> see <a class="ContentNode" href="../../Other/1/2.htm">there</a>.</p>')
    assert "T<sub>u</sub>" in md
    assert "there" in md          # link text kept
    assert "](../" not in md      # cross-pack href dropped
