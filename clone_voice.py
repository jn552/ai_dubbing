from TTS.api import TTS
import ffmpeg
import os
import wave

# to allow torch to load these items
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig 
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs   
from TTS.config.shared_configs import BaseDatasetConfig 

def concat_wave(wav_files, output_path):
    """
    Takes a list of .wav files with similar parameters and concatenates them into one big .wav file

    Args:
        wav_files (list[str]): list of .wav files to be concatenated

    Outputs:
        A single combined .wav file
    """
    audio_data = []

    # concatenating
    for wav in wav_files:
        with wave.open(wav, 'rb') as w:
            if not audio_data:
                params = w.getparams()
            audio_data.append([w.readframes(w.getnframes())])
    
    # saving concatenation to output_path
    with wave.open(output_path, 'wb') as out:
        out.setparams(params)
        for data in audio_data:
            out.writeframes(data[0])


def clone_voice(text_chunks, reference_audio_path, output_path):
    """
    Generates speech audio in the language of text that mimics original voice

    Args: 
        text_chunks (list[str]): Text to be spoken broken into chunks to reduce voice clone drift
        reference_audio_path (str): Path to audio file with speaker's voice
        output_path (str): Path where to save cloned voice audio
    
    Outputs:
        - audio file of translated and cloned speech
    """
    chunk_wav_files = []

    # Load xTTS voice cloning model (works for multiple languages); bypass torch saftey net
    add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])
    tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

    # Convert source audio file to required wav format and temporarily saves to directory (mono, 16kHz, s16)
    wav_path = "temp_speaker.wav"
    ffmpeg.input(reference_audio_path).output(wav_path, ar=16000, ac=1, sample_fmt="s16").run(overwrite_output=True)

    # synthesizing sounds for each chunk
    for index, chunk in enumerate(text_chunks):

        # construct output path for each chunk
        base_name = os.path.splitext(os.path.basename(reference_audio_path))[0] 
        chunk_output_path = os.path.join("outputs", base_name, f"{base_name}.translated.audio{index}.wav")
        chunk_wav_files.append(chunk_output_path)

        # Generate cloned speech and save to output path
        tts_model.tts_to_file(text=chunk, speaker_wav=wav_path, language="zh-cn", file_path=chunk_output_path)
        
    # concatenating each chunk's .wav file into one
    concat_wave(chunk_wav_files, output_path=output_path)

    # delete temporary wave file for soure audio
    if os.path.exists(wav_path):
        os.remove(wav_path)
        
    # delete each chunk's .wav
    for wav in chunk_wav_files:
        if os.path.exists(wav):
            os.remove(wav)
        
    print(f"Saved translated cloned voice audio to: {output_path}")

