import streamlit as st
import whisper


@st.cache_resource
def get_whisper_model():
    return whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    model = get_whisper_model()

    result = model.transcribe(
        audio_path,
        language="ar",
    )

    return result["text"].strip()


if __name__ == "__main__":
    test_audio = (
        "/workspaces/Arabic-Health-Checker/"
        "data/sources/test_voice_note.mp3"
    )

    text = transcribe_audio(test_audio)

    with open(
        "transcription_output.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(text)

    print("Transcription saved to transcription_output.txt")