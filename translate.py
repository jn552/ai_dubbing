import os
import nltk
from transformers import MarianMTModel, MarianTokenizer

nltk.download("punkt_tab")

def translate_text(text_path, source_lang, target_lang):
    """
    Translates text from source langauge to target langage, and saves the translated text into a txt file

    Args:
        text_path (.txt): text file containing text to translate
        source_lang (str): source language code
        target_lag (str): target langage code (e.g., "en", "es", etc.)
    
    Returns:
        - translated text (str)
        - translated chunks in text (list[str]) to reduce voice drift in cloning
    """
    # getting correct langauge codes

    # getting models and tokenizers
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # extracting text from text file
    with open(text_path, "r") as f:
        text = f.read()
    
    # converting tokens and chunking them (prevents tokens from becoming unwieldly)
    input_chunks = nltk.tokenize.sent_tokenize(text) 
    translated_chunks = []

    # translation
    for chunk in input_chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)  # pt for PyTorch
        translated = model.generate(**inputs)
        translated_chunk = tokenizer.decode(translated[0], skip_special_tokens=True)
        translated_chunks.append(translated_chunk)

    translated_text = " ".join(translated_chunks)

    # constructing path to save output to
    base_name = os.path.splitext(os.path.basename(text_path))[0]
    if len(base_name.split(".")) == 2: # only happens if english is used as a bridging language
        base_name = base_name.split(".")[0]
    base_output_dir = "outputs" 
    translated_text_path = os.path.join(base_output_dir, base_name, f"{base_name}.translated.txt")

    # writing translated text (if english used as a bridge between languages, the english translation will be overwritten)
    with open(translated_text_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    return translated_text, translated_chunks

