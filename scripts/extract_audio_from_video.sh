#!/bin/bash

# Check if both arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <input_video.mp4> <output_audio.wav>"
    exit 1
fi

# Extract audio from video
ffmpeg -i "$1" -q:a 0 -map a "$2"