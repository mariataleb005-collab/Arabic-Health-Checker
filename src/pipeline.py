import json

from extract_claims import extract_claims
from generate_verdict import generate_verdict


def check_message(arabic_text: str) -> list[dict]:
    """
    Full text pipeline:
    takes raw Arabic text, extracts health claims,
    and returns a verdict for each claim.
    """

    claims = extract_claims(arabic_text)

    results = []

    for claim in claims:
        verdict = generate_verdict(claim)

        results.append(
            {
                "claim": claim,
                "verdict": verdict,
            }
        )

    return results


def transcribe_voice_note(audio_path: str) -> str:
    """
    Transcribes an Arabic voice note and returns the text.
    Whisper is imported only when this function is called.
    """

    from transcribe import transcribe_audio

    return transcribe_audio(audio_path)


def check_voice_note(audio_path: str) -> list[dict]:
    """
    Voice pipeline:
    transcribes an Arabic voice note,
    then runs the normal text-checking pipeline.
    """

    text = transcribe_voice_note(audio_path)

    print(f"Transcribed text: {text}")

    return check_message(text)


if __name__ == "__main__":
    test_audio = (
        "/workspaces/Arabic-Health-Checker/"
        "data/sources/test_voice_note.mp3"
    )

    results = check_voice_note(test_audio)

    with open(
        "pipeline_output.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            json.dumps(
                results,
                ensure_ascii=False,
                indent=2,
            )
        )

    print(
        f"Checked {len(results)} claim(s) from voice note. "
        "Output saved to pipeline_output.txt"
    )