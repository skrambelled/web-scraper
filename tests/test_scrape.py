from web_scraper.scrape import get_citations_needed_count, get_citations_needed_report


def test_import():
    assert get_citations_needed_count
    assert get_citations_needed_report


def test_count():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    assert get_citations_needed_count(URL) == 1


def test_report():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(URL)
    expect = "---- Citations neeed report ----\n1: Main articles: New Spain and Spanish Empire\n"
    assert actual == expect


def test_general_that_requires_citation_report():
    URL = "https://en.wikipedia.org/wiki/Awara_Zindagi"
    actual = get_citations_needed_report(URL)
    expect = "Article requires citation"
    assert actual == expect


def test_general_that_requires_citation_count():
    URL = "https://en.wikipedia.org/wiki/Awara_Zindagi"
    actual = get_citations_needed_count(URL)
    expect = 1
    assert actual == expect


def test_general_that_does_not_require_citation_report():
    URL = "https://en.wikipedia.org/wiki/Cardiff_Marriott_Hotel"
    actual = get_citations_needed_report(URL)
    expect = "Article does not require citation"
    assert actual == expect


def test_general_that_does_not_require_citation_count():
    URL = "https://en.wikipedia.org/wiki/Cardiff_Marriott_Hotel"
    actual = get_citations_needed_count(URL)
    expect = 0
    assert actual == expect