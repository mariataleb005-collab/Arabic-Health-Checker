import whisper 

model = whisper.load_model("small")

def transcribe_audio (audio_path: str) -> str : 
    """ 
    Takes the path of the audio file and returns its transcribed arabic text
    """
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__" :
    test_audio = "/workspaces/Arabic-Health-Checker/data/sources/test_voice_note.mp3"
    text = transcribe_audio(test_audio)

    with open("transcription_output.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print("Transcription saved to transcription_output.txt")