from openai import OpenAI
from secret import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.with_raw_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini",
)
completion = response.parse().choices
print(completion)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write me a paragraph."}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")