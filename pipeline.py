import sys
import os
from transcribe import transcribe
from translate import translate_text
from clone_voice import clone_voice

def main():
    if len(sys.argv) < 2:
        print("Usage: python pipeline.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]

    # checking file existence
    if not os.path.exists(audio_file):
        print(f"Audio file {audio_file} not found.")
        sys.exit(1)

    base_output_dir = "outputs"
    base_name = os.path.splitext(os.path.basename(audio_file))[0]

    # transcribe
    print("Strating Transcription...")
    transcribe(audio_file)
    transcript_path = os.path.join(base_output_dir, base_name, f"{base_name}.txt")

    # translate
    print("Starting Translation")
    translated_text, translated_chunks = translate_text(transcript_path, source_lang="en", target_lang="zh")

    # save translated text
    translated_text_path = os.path.join(base_output_dir, base_name, f"{base_name}.translated.txt")
    with open(translated_text_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print(f"Translated text saved to {translated_text_path}")

    # generating translated audio with cloned voice
    translated_audio_path = os.path.join(base_output_dir, base_name, f"{base_name}.translated.audio.wav")
    clone_voice(translated_chunks, audio_file, translated_audio_path)

if __name__ == "__main__":
    main()