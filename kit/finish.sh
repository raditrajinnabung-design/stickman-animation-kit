#!/bin/bash

set -e

echo "Starting video finalization..."

if [ "$#" -ne 3 ]; then
    echo "Usage: ./finish.sh input.mp4 audio.mp3 output.mp4"
    exit 1
fi

VIDEO="$1"
AUDIO="$2"
OUTPUT="$3"

python3 "$(dirname "$0")/mix.py" "$VIDEO" "$AUDIO" "$OUTPUT"

echo "Video successfully completed!"
echo "Output: $OUTPUT"
