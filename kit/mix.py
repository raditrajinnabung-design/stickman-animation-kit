import subprocess
import argparse

def mix_audio(video, audio, output):
    command = [
        "ffmpeg",
        "-y",
        "-i", video,
        "-i", audio,
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output
    ]

    subprocess.run(command, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("audio")
    parser.add_argument("output")

    args = parser.parse_args()

    mix_audio(args.video, args.audio, args.output)
