

import json
import xmltojson
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from datetime import datetime


def get_page_from_url(url):
    try:
        url_search = urlopen(url)
    except Exception as e:
        print("get_page_from_url 1 ", e)
        return None, e

    page = url_search.read()

    # get html from beautifulsoup
    html_code = bs(page, "html.parser")

    # load html plaintext into json
    try:
        json_code = xmltojson.parse(html_code.prettify())
        json_data = json.loads(json_code)
    except Exception as e:
        print("get_page_from_url 2 ", e)
        return None, e

    return json_data, None


if __name__ == "__main__":
    get_page_from_url("https://en.wikipedia.org/wiki/Website")

