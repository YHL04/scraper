

from search import get_page_from_url, get_texts_from_page, web_search
from gpt import *


persons = []
searches = []
errors = []
new_persons = []
summary = []


def read_people(filename="backup.txt"):
    global persons
    global searches

    with open(filename) as file:
        persons = [line.rstrip() for line in file]
        searches = [p.split(",")[0] for p in persons]


def get_profiles():
    global persons
    global errors
    global new_persons
    global summary

    for i, p in enumerate(persons):
        texts = ""

        # get websites and concatenate them
        urls = web_search(searches[i], num_results=2)
        for u in urls[:10]:
            page, error = get_page_from_url(u)
            if error is not None:
                errors += str(error)
            if page is not None:
                text = get_texts_from_page(page)
                text = " NEW PAGE: ".join(text)
                texts += text

        # get current and past location
        if find_location_from_query(texts, location="Beijing, China"):
            summary.append(better_summarize_people_from_query(texts, p)[0])
            new_persons.append(people_from_query(texts, persons)[0])


if __name__ == "__main__":
    read_people()
    print(persons)
    get_profiles()

    for s in summary:
        print(s)
    for n in new_persons:
        print(n)
