import google.generativeai as genai
from .secret import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5")


def query_gemini(query):
    """
    Args:

    Returns:

    """
    return [model.generate_content(query).text]
