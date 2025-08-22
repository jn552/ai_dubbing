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

1. Clone the repo and run `cd ai_dubbing` to enter the repo.

'''bash
git clone https://github.com/yourusername/ai_dubbing.git
cd ai_dubbing

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

3. Set up 

# Future Work / Improvements

for myself:

pyenv activate wav2lip-py37
source ai_dub_env/bin/activate
