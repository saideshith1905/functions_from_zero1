import wikipedia
from yake import KeywordExtractor


# build a finction to return the summary of a wikipedia page


def get_wiki_summary(page):
    """
    Return the summary of a wikipedia page
    """
    return wikipedia.summary(page)


# build a finction to search wikipedia pages for a match


def search_wiki_pages(page):
    """ "
    Search wikipedia pages for a match
    """
    return wikipedia.search(page)


# build a function to return the wikipedia page
def get_wiki_page(page):
    """
    Return the wikipedia page
    """
    return wikipedia.page(page)


# return keyords of the wikipeida page


def get_wiki_keywords(page):
    """
    Return the keywords of a wikipedia page
    """
    content = get_wiki_page(page).content
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    return {keyword: score for keyword, score in keywords[:10]}
