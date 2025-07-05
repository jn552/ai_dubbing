import torch
from TTS.api import TTS
import ffmpeg
import os

# to allow torch to load these items
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig 
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs   
from TTS.config.shared_configs import BaseDatasetConfig 

def clone_voice(text, reference_audio_path, output_path):
    """
    Generates speech audio in the language of text that mimics original voice

    Args: 
        text (str): Text to be spoken
        reference_audio_path (str): Path to audio file with speaker's voice
        output_path (str): Path where to save cloned voice audio
    
    Outputs:
        - audio file of translated and cloned speech
    """
    # Load xTTS voice cloning model (works for multiple languages); bypass torch saftey net
    add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])
    tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

    # Convert audio file to required wav format (mono, 16kHz, s16)
    wav_path = "temp_speaker.wav"
    ffmpeg.input(reference_audio_path).output(wav_path, ar=16000, ac=1, sample_fmt="s16").run(overwrite_output=True)

    try:
        # Generate cloned speech and save to output path
        tts_model.tts_to_file(text=text, speaker_wav=wav_path, language="zh-cn", file_path=output_path)
    finally:
        # Cleanup temporary wav file
        if os.path.exists(wav_path):
            os.remove(wav_path)

    print(f"Saved translated cloned voice audio to: {output_path}")

