import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # You can choose from "tiny", "base", "small", "medium", "large"
    result = model.transcribe(audio_file)
    return result['text']