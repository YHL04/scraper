

from googlesearch import search


def web_search(query, num_results):
    """
    'list' object has no attribute 'timeout'
    """
    top_results = search(query, num_results=num_results)

    ans = []
    for result in top_results:
        ans.append(result)

    return ans


if __name__ == "__main__":
    results = web_search("Python", num_results=10)
    print(results)
