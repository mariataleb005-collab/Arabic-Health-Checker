import json
import os

import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv

from retrieve import retrieve_relevant_chunks


load_dotenv()


@st.cache_resource
def get_client():
    return Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )


SYSTEM_PROMPT = """
You are a careful, respectful Arabic-language medical fact-checking assistant.

You will be given a health claim and several retrieved reference passages,
each labeled with its source file.

Some passages may not actually be relevant to the claim. Ignore any that
do not directly address it, and do not force a connection that is not there.

Using only the passages that are genuinely relevant, respond with ONLY
a JSON object with these fields:

- "verdict": one of:
  "مؤكد صحيح",
  "مؤكد خاطئ",
  "صحيح جزئيًا",
  "معلومات غير كافية"

- "explanation":
  a short, respectful, plain Arabic explanation of 2-3 sentences

- "risk_level": one of:
  "منخفض",
  "متوسط",
  "عالي"

- "sources_used":
  a list of source filenames that were actually relevant.
  Return an empty list if none were relevant.

Return JSON only.
No markdown.
No explanation outside the JSON object.
"""


def generate_verdict(claim: str) -> dict:
    client = get_client()

    chunks = retrieve_relevant_chunks(claim)

    context = "\n\n".join(
        f"[Source: {chunk['source']}]\n{chunk['text']}"
        for chunk in chunks
    )

    user_message = (
        f"Claim: {claim}\n\n"
        f"Retrieved passages:\n{context}"
    )

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
    )

    raw_output = next(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()

    if raw_output.startswith("```"):
        raw_output = raw_output.split("```")[1]
        raw_output = raw_output.removeprefix("json").strip()

    try:
        verdict = json.loads(raw_output)

    except json.JSONDecodeError:
        print("⚠️ Model didn't return valid JSON. Raw output was:")
        print(raw_output)
        return {}

    return verdict


if __name__ == "__main__":
    test_claim = "زيادة الوزن تزيد من خطر الإصابة بالسكري"

    result = generate_verdict(test_claim)

    with open(
        "verdict_output.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            json.dumps(
                result,
                ensure_ascii=False,
                indent=2,
            )
        )

    print(
        "Verdict saved to verdict_output.txt — "
        "open it in VS Code's editor to read the Arabic properly."
    )