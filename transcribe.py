import os
import json
from whisper import load_model

def transcribe(audio_path, base_output_dir="outputs", model_name="small"):
    """
    Transcribes an audio file using OpenAI's Whisper model and saves the output

    Args:
        audio_path (str): Path to input audio file
        base_output_dir (str): Directory where output folders will be created
        model_name (str): Name of the Whisper model to use (e.g., "tiny", "base", "small", ..., "large")

    Outputs:
        - plain text transcript (.txt)
        - full JSON result with segments, timestamps, etc.
        All saved in a subfolder named after the input file without its extension
    """

    base_name = os.path.splitext(os.path.basename(audio_path))[0]  # grabs filename, splits name and extension, grabs name only
    output_dir = os.path.join(base_output_dir, base_name)  
    os.makedirs(output_dir, exist_ok=True)

    # loading model and transcribing
    model = load_model(model_name)
    print(f"Transcribing: {audio_path} using Whisper model: {model_name}")
    result = model.transcribe(audio_path)

    # saving transcription as plain txt file
    txt_path = os.path.join(output_dir, f"{base_name}.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Saved transcript to {txt_path}")

    # save full reslt as JSON
    json_path = os.path.join(output_dir, f"{base_name}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)  # indent 2 for readability
    print(f"Saved entire transcription JSON to {json_path}")

def main():
    audio_file = "testing_whisper.m4a"
    transcribe(audio_file)

if __name__ == "__main__":
    main()
