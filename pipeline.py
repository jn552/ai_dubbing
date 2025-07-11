import sys
import os
from transcribe import transcribe
from translate import translate_text
from clone_voice import clone_voice
from lip_sync import lip_sync
from extract_audio import extract_audio_from_video
from get_iso_codes import get_iso_code

def main():

    if len(sys.argv) < 5:
        print("Usage: python pipeline.py <audio|video> <audio_file|video_file> <source_lang> <target_lang>")
        sys.exit(1)

    # extracting system arguments
    mode = sys.argv[1]
    file = sys.argv[2]
    source_lang = sys.argv[3]
    target_lang = sys.argv[4]

    # checking language compatability
    if source_lang not in ["english", "mandarin", "french", "german", "russian", "korean", "arabic", "japanese", "italian"]:
        print("Unsupported Language: choose from english, mandarin, french, german, russian, korean, arabic, japanese, or italian")
        sys.exit(1)
    if target_lang not in ["english", "mandarin", "french", "german", "russian", "korean", "arabic", "japanese", "italian"]:
        print("Unsupported Language: choose from english, mandarin, french, german, russian, korean, arabic, japanese, or italian")
        sys.exit(1)

    # checking file existence
    if not os.path.exists(file):
        print(f"Audio/Video file {file} not found.")
        sys.exit(1)
    
    # getting ISO codes for language
    source_lang = get_iso_code(source_lang)
    target_lang = get_iso_code(target_lang)

    base_output_dir = "outputs"
    base_name = os.path.splitext(os.path.basename(file))[0]
    output_dir = os.path.join(base_output_dir, base_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Seperating audio and video
    if mode == "audio":  # audio is mp4 or m4a
        audio_file = file
        video_file = None
    elif mode == "video":
        video_file = file
        audio_file = os.path.join(output_dir, f"{base_name}.wav")  # extracted audio is a wav file
        extract_audio_from_video(video_file, audio_file)
    else:
        print("Invalid Mode; Usage: python pipeline.py <audio//video> <audio_file//video/file>")
        sys.exit(1)

    # transcribe
    print("Starting Transcription...")
    transcribe(audio_file)
    transcript_path = os.path.join(output_dir, f"{base_name}.txt")

    # translate
    print("Starting Translation")
    if source_lang == "en" or target_lang=="en":
        translated_text, translated_chunks = translate_text(transcript_path, source_lang=source_lang, target_lang=target_lang)
    else: # if english is not involved, use english to bridge the two languages (bridging english translation is saved as a text file)
        translated_text, _ = translate_text(transcript_path, source_lang=source_lang, target_lang="en")
        translated_text, translated_chunks = translate_text(os.path.join(output_dir, f"{base_name}.translated.txt"), source_lang="en", target_lang=target_lang)


    # save translated text
    translated_text_path = os.path.join(output_dir, f"{base_name}.translated.txt")
    with open(translated_text_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print(f"Translated text saved to {translated_text_path}")

    # generating translated audio with cloned voice
    translated_audio_path = os.path.join(output_dir, f"{base_name}.translated.audio.wav")
    clone_voice(translated_chunks, audio_file, translated_audio_path, target_lang)

    # further instructions if video was provided
    if mode == "video":
        print(f"Activate the seperate pyenv and run lip_sync_pipe.py with: python lip_sync_pipe.py {base_name}.translated.audio.wav {video_file}")
    

if __name__ == "__main__":
    main()