

keywords = ["vertical-align", "padding:", "dateModified", "https", "http", "transientcontent", ".png", "@media",
            ".div", "tags", "csrfToken", "client-nojs", "vector-dropdown-label", "load.php", "skin-vector",
            "vector-search-box-vue", "search-toggle", "index.php", ".mw-parser-output"]


def process_html_url(html, text, length=100):
    """
    Process html text recursively in the form of json
    """
    if html is None:
        return []

    if type(html) == dict:
        html = [html[key] for key in list(html.keys())]

    for e in html:
        if type(e) == dict or type(e) == list:
            text = process_html_url(e, text, length=length)
        elif type(e) == str and len(e) > length:
            text.append(e)

    return text


def filter_keyword(arr, keyword):
    """
    Filter out strings in arr if it contains keyword
    """
    ans = []
    for a in arr:
        assert type(a) == str, type(a)

        if keyword not in a:
            ans.append(a)

    return ans


def filter_keywords(arr):
    """
    A wrapper to filter many keywords at once
    """
    for keyword in keywords:
        arr = filter_keyword(arr, keyword=keyword)

    return arr


def get_texts_from_page(html):
    """
    Given html in the form of json, extract out important text
    """
    text = process_html_url(html, [])
    text = filter_keywords(text)

    return text


if __name__ == "__main__":
    from urls import get_page_from_url

    u = get_page_from_url("https://en.wikipedia.org/wiki/Ministry_of_State_Security_(China)")
    text = process_html_url(u, [])
    text = filter_keywords(text)
    print(text)
