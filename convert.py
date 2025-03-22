import whisper
import sys
import os

audio_file = "audio.wav"

if len(sys.argv) >= 2:
    audio_file = sys.argv[1]

model = whisper.load_model("base")  # You can choose from "tiny", "base", "small", "medium", "large"
result = model.transcribe(audio_file)

output_file = os.path.splitext(audio_file)[0] + ".md"
with open(output_file, "w") as f:
    f.write(result['text'])

print(f"Transcription written to {output_file}")