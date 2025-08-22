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

# Installation and Usage

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

5. **Install dependencies** in the second virtual environment
```bash
pip install -r lip_sync_requirements.txt
```


# Future Work / Improvements

for myself:

pyenv activate wav2lip-py37
source ai_dub_env/bin/activate
