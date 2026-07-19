"""Tests for anchor slugs and cross-reference resolution (no third-party deps)."""
from siemenshelp.links import (
    _href_to_itemid,
    github_slug,
    make_corpus_resolver,
    make_resolver,
    uniq_slugger,
)


def test_github_slug_basic():
    assert github_slug("PID control") == "pid-control"
    assert github_slug("Auxiliary functions (S7-1200, S7-1500)") == "auxiliary-functions-s7-1200-s7-1500"
    assert github_slug("  Trailing/leading  ") == "trailingleading"


def test_uniq_slugger_dedupes_like_github():
    slug = uniq_slugger()
    assert slug("Overview") == "overview"
    assert slug("Overview") == "overview-1"
    assert slug("Overview") == "overview-2"
    assert slug("Other") == "other"


def test_resolver_same_pack_anchor():
    resolve = make_resolver({"19912525195.htm": "pulse-controller"})
    assert resolve("19912525195.htm") == "#pulse-controller"
    # query/fragment are ignored when matching the file
    assert resolve("19912525195.htm?x=1#frag") == "#pulse-controller"


def test_resolver_cross_pack_and_external():
    resolve = make_resolver({"a.htm": "a"})
    assert resolve("../../OtherPack/1/2.htm") is None      # cross-pack -> Phase 2
    assert resolve("unknown.htm") is None                   # not in this pack
    assert resolve("https://siemens.com") == "https://siemens.com"
    assert resolve("#existing") == "#existing"
    assert resolve("") is None
    assert resolve(None) is None


def test_href_to_itemid():
    assert _href_to_itemid("../../P/9/x.htm") == "P/9/x.htm"
    assert _href_to_itemid("../../P/9/x.htm#frag") == "P/9/x.htm"
    assert _href_to_itemid("x.htm?culture=en-US") == "x.htm"


def test_corpus_resolver_same_and_cross_pack():
    file_to_anchor = {"a.htm": "topic-a"}
    id_to_target = {"OtherPack/9/x.htm": ("Other Section", "some-heading")}
    resolve = make_corpus_resolver(file_to_anchor, id_to_target)
    # same-pack -> local anchor
    assert resolve("a.htm") == "#topic-a"
    # cross-pack in corpus -> percent-encoded file + anchor
    assert resolve("../../OtherPack/9/x.htm") == "Other%20Section.md#some-heading"
    # cross-pack not in corpus -> None (render as text)
    assert resolve("../../Unknown/1/2.htm") is None
    assert resolve("https://siemens.com") == "https://siemens.com"
