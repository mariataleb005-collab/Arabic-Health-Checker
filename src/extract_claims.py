

import json
import os

import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()


@st.cache_resource
def get_client():
    return Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )


SYSTEM_PROMPT = """
You are a precise information-extraction tool.

Given Arabic text, identify each distinct factual health claim it contains.

Return ONLY a JSON array of strings, one per claim, in Arabic.
No explanation, no markdown, just the JSON array.

If there are no health claims, return an empty array.
"""


def extract_claims(arabic_text: str) -> list[str]:
    """
    Takes raw Arabic text and returns a list of health claims found in it.
    """

    client = get_client()

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": arabic_text,
            }
        ],
    )

    raw_output = next(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()

    # Extra protection in case the model wraps JSON in a code block.
    if raw_output.startswith("```"):
        raw_output = raw_output.split("```")[1]
        raw_output = raw_output.removeprefix("json").strip()

    try:
        claims = json.loads(raw_output)

    except json.JSONDecodeError:
        print("Model didn't return valid JSON. Raw output was:")
        print(raw_output)
        return []

    return claims


if __name__ == "__main__":
    sample_text = (
        "شرب الماء الدافئ بالليمون ينشط الجسم، "
        "وبعض الناس يقولون إن الصيام المتقطع يعالج السكري نهائيًا"
    )

    claims = extract_claims(sample_text)

    print("Extracted claims:")

    for claim in claims:
        print(" -", claim)