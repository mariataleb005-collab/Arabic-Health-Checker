"""
Run this file directly to test it:
    python src/extract_claims.py
"""

import os
from dotenv import load_dotenv

load_dotenv()  # reads your .env file so the API key is available

def extract_claims(arabic_text: str) -> list[str]:
    """
    Takes raw Arabic text and returns a list of health claims found in it.
    Right now this is just a placeholder — we'll build the real logic together.
    """
    raise NotImplementedError("We'll build this together in Week 1!")


if __name__ == "__main__":
    sample_text = "الزنجبيل يشفي من السرطان وأحسن من الكيماوي"
    claims = extract_claims(sample_text)
    print(claims)
