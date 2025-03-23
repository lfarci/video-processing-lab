import sys
import ffmpeg

def extract_audio(input_video: str, output_audio: str) -> None:
    """
    Extract audio from a video file and save it as a WAV file.
    
    Args:
        input_video (str): Path to the input video file
        output_audio (str): Path where the output audio will be saved
    """
    try:
        stream = ffmpeg.input(input_video)
        stream = ffmpeg.output(stream, output_audio, acodec='pcm_s16le', ac=1, ar='16k')
        ffmpeg.run(stream, overwrite_output=True)
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}", file=sys.stderr)
        sys.exit(1)