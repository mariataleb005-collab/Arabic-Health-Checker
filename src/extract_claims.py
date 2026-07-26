"""
Run this file directly to test it:
    python src/extract_claims.py
"""

import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  

client = Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a precise information-extraction tool. Given Arabic text, identify each distinct factual health claim it 
contains. Return ONLY a JSON array of strings, one per claim, in Arabic. No explanation, no markdown,
 just the JSON array. If there are no health claims, return an empty array."""

def extract_claims(arabic_text: str) -> list[str]:
    """
    Takes raw Arabic text and returns a list of health claims found in it.
    """
    response = client.messages.create(
        model = "claude-sonnet-5",
        max_tokens=500,
        system = SYSTEM_PROMPT, #gives the instruction separately from the data
        messages=[
            {"role" : "user" , "content" : arabic_text}
        ]
    )

    #raw_output = response.content[0].text.strip()
    raw_output = next(
    block.text for block in response.content if block.type == "text").strip()
    
    if raw_output.startswith("```"):
        raw_output = raw_output.split("```")[1]
        raw_output = raw_output.removeprefix("json").strip()
        
    try:
        claims = json.loads(raw_output) #converts the model's text response into python list
    except json.JSONDecodeError:
        print("Model didn't return a valid json. Raw output was: ")
        print(raw_output)
        return[]

    return claims


if __name__ == "__main__":
    sample_text = "شرب الماء الدافئ بالليمون ينشط الجسم، وبعض الناس يقولون إن الصيام المتقطع يعالج السكري نهائيًا"
    claims = extract_claims(sample_text)
    print("Extracted claims:")
    for c in claims:
        print(" -", c)