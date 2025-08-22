# AI Dubbing
Automatically translate and dub yourself speaking a different language with lip syncing

# DEMO
**English to Mandarin:**

Original: https://youtube.com/shorts/Pe4mbbjg5lU &nbsp; &nbsp; &nbsp; Dubbed: https://youtube.com/shorts/Qd9mpZNbZvc

**Mandarin to Spanish:**

Original: https://youtu.be/F0AdsF_iZOg &nbsp; &nbsp; &nbsp; Dubbed: https://youtu.be/p45HXBzTQLw

# Features
Automatic speech-to-text – Uses **Whisper** to convert audio from videos into transcripts.

Multilingual translation – Uses **MarianMT** to support translation into multiple languages.

Voice cloning & dubbing – Uses **Coqui TTS** to generate target language speech in the users voice.

Lip-sync video generation – Uses **Wav2Lip** to align dubbed audio with video lip movements.

Suported Languages: English, Mandarin, French, German, Russian, Korean, Arabic, Japanese, Spanish, or Italian

# Installation

1. **Clone the repository** and enter the project folder:

```bash
git clone https://github.com/yourusername/ai_dubbing.git
cd ai_dubbing
```

2. **Create the first virtual environment** (this program requires two separate environments due to dependency conflicts) and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

3. **Install dependencies** in the first environment:
```bash
pip install -r requirements.txt
```

4. **Deactivate the first virtual environment** and create the second one (using pyenv with Python 3.7.9) for lip syncing:
```bash
pyenv install 3.7.9
pyenv virtualenv 3.7.9 lip_venv
pyenv activate lip_venv
```

5. **Install dependencies** in the second virtual environment for lip syncing
```bash
pip install -r lip_sync_requirements.txt
```

# Usage
1. Activate first virtual environment and run:
 ```bash
python pipeline.py <audio/video> <audio_file/video_file> <source_language> <target_language>
```
 Pick audio if you just want to dub an audio file and video if you want to dub a full video.

 Supported source and target languages (enter in lowercase): english, mandarin, french, german, russian, korean, arabic, japanese, spanish, or italian

2. Activate second virtual environment (the lip sync one) and run the command that gets outputted after runnning the first python script. When the scirpt finishes, the output should be saved in the outputs folder.

# Future Work / Improvements

1. Sometimes the length of the translated audio is longer/shorter than the original leading to mismatched lip movement. Potential fixes could include chunking the video into smaller segments and aligning lip moements in each chunk before concatenating into one larger video.

2. Adding a low resource langauge such as Cantonese option would be nice. This could be implemented by finetuning the existing Mandarin model with open source Cantonese data, or data from my friends/family
