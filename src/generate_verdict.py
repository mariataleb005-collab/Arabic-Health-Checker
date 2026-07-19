import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic
from retrieve import retrieve_relevant_chunks

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a careful, respectful Arabic-language medical fact-checking assistant.

You will be given a health claim and several retrieved reference passages, each labeled with its source file. Some passages may not actually be relevant to the claim — ignore any that don't directly address it, and don't force a connection that isn't there.

Using only the passages that are genuinely relevant, respond with ONLY a JSON object (no markdown, no explanation outside it) with these fields:
- "verdict": one of "مؤكد صحيح", "مؤكد خاطئ", "صحيح جزئيًا", "معلومات غير كافية"
- "explanation": a short, respectful, plain Arabic explanation (2-3 sentences), avoiding a judgmental tone
- "risk_level": one of "منخفض" (harmless folk wisdom), "متوسط", "عالي" (dangerous if believed and acted on)
- "sources_used": a list of the source filenames that were actually relevant (empty list if none were)
"""


def generate_verdict(claim: str) -> dict:
    chunks = retrieve_relevant_chunks(claim)

    context = "\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )

    user_message = f"Claim: {claim}\n\nRetrieved passages:\n{context}"

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}]
    )

    raw_output = response.content[0].text.strip()
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

    with open("verdict_output.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=2))

    print("Verdict saved to verdict_output.txt — open it in VS Code's editor to read the Arabic properly.")