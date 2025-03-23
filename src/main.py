from audio import transcribe_audio, extract_audio
from langchain_ollama.llms import OllamaLLM
from data import get_all_mp4_url

import sys
import os
import requests

def write_transcription_to_file(audio_file, transcription):
    output_file = os.path.splitext(audio_file)[0] + ".md"
    with open(output_file, "w") as f:
        f.write(transcription)
    print(f"Transcription written to {output_file}")

def download_mp4(url, output_path):
    """Download MP4 file from URL to the specified path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    mp4_urls = get_all_mp4_url(json_file_path)

    for mp4_url in mp4_urls:
        print(f"Downloading {mp4_url}...")

        if download_mp4(mp4_url, "temp.mp4"):
            print(f"Downloaded {mp4_url} to temp.mp4")
            print("Extracting audio...")
            audio_file = extract_audio("temp.mp4", "temp.wav")
            print(f"Audio extracted to {audio_file}")

    # transcription = transcribe_audio(audio_file)
    # write_transcription_to_file(audio_file, transcription)

    # llm = OllamaLLM(model="mistral:latest")

    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         print("Exiting chat.")
    #         break

    #     for token in llm.stream(user_input):
    #         print(token, end='', flush=True)

    #     print()  # for a new line after the response
