

from .gemini import *
from .gemma import *
from .gpt4o import *


def get_query(query):
    """
    Args:

    Returns:

    """
    return query_gpt4o(query)
    # return query_gemini(query)


def summarize_from_query(query):
    """
    Args:

    Returns:

    """
    new_query = "Please summarize this website in 2-3 sentences. Do not give unnecessary text. Also skip over" \
                " the general overview such as the overall description of an organization (general knowledge)" \
                " WEBSITE: {}".format(query)

    completions = get_query(new_query)
    return completions


def bullet_points_from_query(query, context):
    """
    Args:

    Returns:

    """
    new_query = "Please give bullet points related to this website one sentence each that do not overlap existing" \
                " points. Also skip over the general overview such as the overall description of an organization " \
                "(general knowledge) Do not give text if the website is down. WEBSITE: {} QUERIES: " \
                "".format(query, context)

    completions = get_query(new_query)
    return completions


def people_from_query(query, context):
    """
    Args:

    Returns:

    """
    new_query = "Please give names of people related to this website one line each that do not overlap existing" \
                " names. Also, give a one sentence description of what they do. "\
                " Do not give text if the website is down. WEBSITE: {} KNOWN NAMES: " \
                "".format(query, context)

    completions = get_query(new_query)
    return completions


def find_location_from_query(query, location):
    """
    Args:

    Returns:

    """
    new_query = "Say TRUE of the persons related to the websites are located in {} or has located in {}" \
                " otherwise say FALSE. WEBSITE TEXT: ".format(location, location, query)

    completions = get_query(new_query)
    if completions[0] == "TRUE":
        return True
    elif completions[0] == "FALSE":
        return False
    else:
        return True


def summarize_people_from_query(query):
    """
    Args:

    Returns:

    """
    new_query = "Please give the summary of people in the form of NAME, DESCRIPTION where each line is a new person: " \
                "Do not give unnecessary characters such as * or -, make it like a .csv file so it is ready to be read" \
                " as a .csv file. They have to be REAL people. CONTEXT: {}".format(query)

    completions = get_query(new_query)
    return completions


def better_summarize_people_from_query(query, context):
    """
    Args:

    Returns:

    """
    new_query = "Please give the summary of people in the form of NAME, CURRENT_LOCATION, CURRENT_ORGANIZATION, " \
                "DESCRIPTION (3-5 sentences) where the answer is 'unknown' if it can not be determined. " \
                "Do not give unnecessary characters such as * or -, make it like a .csv file so it " \
                "is ready to be read as a .csv file. They have to be REAL people. TEXT: {} HAS TO BE RELATED TO: {} " \
                "NOTE THAT there are many website of different people with the same name that are irrelevant and " \
                "should not be summarized".format(query, context)

    completions = get_query(new_query)
    return completions


def find_query_from_objective(query):
    """
    Args:

    Returns:

    """
    new_query = "Please give some ideas that will contribute to the goal, use : to separate each idea so it can be" \
                " separated by the code. Do not give unnecessary text. Goal: {} BEGIN HERE: ".format(query)

    completions = get_query(new_query)

    ideas = []
    for c in completions:
        ideas.extend(c.split(":"))

    return ideas


def find_search_query_from_objective(query, t=1.):
    """
    Args:

    Returns:

    """
    new_query = "Please give some search queries that are related to the context, use : to separate each query " \
                "so it can be separated by the code. Do not give unnecessary text. Context: {} " \
                "BEGIN HERE: ".format(query)

    completions = get_query(new_query)

    ideas = []
    for c in completions:
        ideas.extend(c.split(":"))

    return ideas


def find_search_query_from_goal(query, t=1.):
    """
    Args:

    Returns:

    """
    new_query = "Please give some search queries that are related to the goal, use : to separate each query " \
                "so it can be separated by the code. Do not give unnecessary text. Goal: {} " \
                "BEGIN HERE: ".format(query)

    completions = get_query(new_query)

    ideas = []
    for c in completions:
        ideas.extend(c.split(":"))

    return ideas

