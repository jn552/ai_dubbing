import os
import nltk
from transformers import MarianMTModel, MarianTokenizer

nltk.download("punkt_tab")

def translate_text(text_path, source_lang, target_lang):
    """
    Translates text from source langauge to target langage

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

    return " ".join(translated_chunks), translated_chunks

def main():
    
    # constructing path to save output to
    base_name = "testing_whisper"
    output_dir = "outputs" 
    translated_text_path = os.path.join(output_dir, base_name, f"{base_name}.translated.txt")

    # translating
    text_path = os.path.join(output_dir, base_name, f"{base_name}.txt")
    translated_text = translate_text(text_path=text_path)

    with open(translated_text_path, "w", encoding="utf-8") as f:
        f.write(translated_text)
    
if __name__ == "__main__":
    main()


    
