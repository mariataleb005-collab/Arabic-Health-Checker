import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Reply with just the word: connected"}
    ]
)

print(response.content[0].text)