from conversion import transcribe_audio
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    transcription = transcribe_audio(audio_file)

    output_file = os.path.splitext(audio_file)[0] + ".md"
    with open(output_file, "w") as f:
        f.write(transcription)

    print(f"Transcription written to {output_file}")
