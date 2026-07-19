import json
from extract_claims import extract_claims
from generate_verdict import generate_verdict


def check_message(arabic_text: str) -> list[dict]: 
    """
    Full pipeline: takes raw Arabic text, extracts claims,
    and returns a verdict for each one.
    """
    claims = extract_claims(arabic_text)

    results = []
    for claim in claims:
        verdict = generate_verdict(claim)
        results.append({"claim": claim, "verdict": verdict})

    return results


if __name__ == "__main__":
    test_message = "شرب الزنجبيل يشفي من السرطان، وزيادة الوزن تزيد من خطر الإصابة بالسكري"

    results = check_message(test_message)

    with open("pipeline_output.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(results, ensure_ascii=False, indent=2))

    print(f"Checked {len(results)} claim(s). Output saved to pipeline_output.txt")