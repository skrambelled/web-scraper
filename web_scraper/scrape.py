import requests
from bs4 import BeautifulSoup

assert requests
assert BeautifulSoup

def _get_soup(URL):
    """
    helper function to handle HTTP requests and parse them into BeautifulSoup objects
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def _general_citations_needed(URL):
    """
    Some wikipedia pages require citations but do not state precisely where they are needed
    So this is a helper function for handling those cases
    """
    soup = _get_soup(URL)
    results = soup.find('table', class_='box-More_citations_needed')
    if results:
        return True
    else:
        return False


def get_citations_needed_count(URL):
    """
    return a count of how many "citations needed" flags there are on any given wikipedia page
    """
    soup = _get_soup(URL)
    results = soup.find_all('a', href='/wiki/Wikipedia:Citing_sources')

    general = _general_citations_needed(URL)

    count = 0
    for result in results:
        if result.text == 'cite':
            count += 1
    
    if count:
        return count
    elif general:
        return 1
    return 0
    

def get_citations_needed_report(URL):
    """
    return string of 'passages' that any given wikipedia page has flagged as needing citations
    """
    soup = _get_soup(URL)
    results = soup.find_all('a', href='/wiki/Wikipedia:Citing_sources')

    general = _general_citations_needed(URL)

    articles = "---- Citations neeed report ----\n"
    count = 0
    for result in results:
        if result.text == 'cite':
            count += 1
            prev_sibling = result.find_parent('table', class_="ambox-Unreferenced").find_previous_sibling()
            articles += str(count) + ": " + prev_sibling.text + "\n"
    
    if count:
        return articles
    elif general:
        return "Article requires citation"
    return "Article does not require citation"
