

from search import get_page_from_url, get_texts_from_page, web_search
from gpt import *

"""
query("Write me a paragraph")
find_query_from_objective("Find the address of Ministry of State Security")
find_search_query_from_objective("Ministry of State Security")
"""

counter = 0
used_urls = []
inaccessible_urls = []
ans = ""
errors = ""


def get_intel(query="Ministry of State Security"):
    global used_urls
    global inaccessible_urls
    global counter
    global ans
    global errors

    if counter % 10 == 0:
        summarize_intel()

    if counter > 100:
        return

    queries = find_search_query_from_objective(query=query)

    for q in queries[:20]:
        urls = web_search(q, num_results=2)
        print("QUERY: {}".format(q))

        urls = [u for u in urls if u not in used_urls]
        for url in urls:
            counter += 1
            used_urls.append(url)
            page, error = get_page_from_url(url)
            if error is not None:
                errors += str(error)
            if page is not None:
                text = get_texts_from_page(page)

                print("URL: {}".format(url))
                # a = bullet_points_from_query_gpt4o(text, ans)[0]
                a = people_from_query(text, ans)[0]
                print(a)
                ans += a
                new_queries = find_search_query_from_objective(query="{} {}".format(query, text))
                for new_q in new_queries:
                    get_intel(new_q)

            else:
                inaccessible_urls.append(url)
                print("INACCESSIBLE URLS: {}".format(len(inaccessible_urls)))
                print("COUNTER: {}".format(counter))


def summarize_intel():
    global ans
    global errors

    print(ans)
    ret = summarize_people_from_query(ans)[0]
    print(ret)

    with open("people.txt", "w+") as f:
        f.write(ret)

    with open("errors.txt", "w+") as f:
        f.write(errors)


if __name__ == "__main__":
    get_intel()
    summarize_intel()

