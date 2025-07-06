import subprocess

def extract_audio_from_video(video_path, output_audio_path):
    """
    Extracts the audio from a video and saves as a .wav file
    """

    command = ["ffmpeg",
               "-y",
               "-i", video_path,
               "-ac", "1",
               "-ar", "16000",
               output_audio_path
    ]

    print(f"Extracting audio from video")

    result = subprocess.run(command, capture_output=True, text=True)

    # messages to determine if extraction is complete
    if result.returncode != 0:
        print("Audio extraction error:\n", result.stderr)
        raise RuntimeError("Failed to extract audio from video")
    else:
        print("Audio extracted successfully.")