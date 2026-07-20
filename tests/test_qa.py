"""Tests for the corpus linter."""
from siemenshelp.qa import lint_corpus


def test_qa_clean_corpus(tmp_path):
    (tmp_path / "A.md").write_text("# Title A\n\n## Sub\n\nSee [ok](#sub).\n")
    report = lint_corpus(str(tmp_path))
    assert report["files"] == 1
    assert report["issues"] == {}


def test_qa_detects_broken_intra_anchor(tmp_path):
    (tmp_path / "A.md").write_text("# Title A\n\n## Sub\n\nSee [bad](#nope).\n")
    report = lint_corpus(str(tmp_path))
    assert report["issues"].get("broken_intra_anchor") == 1


def test_qa_detects_broken_cross_file_link(tmp_path):
    (tmp_path / "A.md").write_text("# A\n\nSee [x](Missing.md#h).\n")
    report = lint_corpus(str(tmp_path))
    assert report["issues"].get("broken_link_target_missing") == 1


def test_qa_detects_leftover_html_tag(tmp_path):
    # A raw <Operand> outside code is a leaked placeholder; <sub>/<sup>/<br> are ok.
    (tmp_path / "A.md").write_text("# A\n\nUse <Operand> here. Keep T<sub>u</sub>.\n")
    report = lint_corpus(str(tmp_path))
    assert report["issues"].get("leftover_html_tag") == 1
