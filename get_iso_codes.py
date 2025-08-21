def get_iso_code(language):
    """
    Takes the name of a langage and converts it into the appropriate ISO code
    for the Marian models

    Args:
        language (str) : Name of langauge

    Returns:
        lang_code (str) : ISO code for language
    """
    if language == "english":
        lang_code = "en"
    elif language == "mandarin":
        lang_code = "zh"
    elif language == "spanish":
        lang_code = "es"
    elif language == "french":
        lang_code = "fr"
    elif language == "german":
        lang_code = "de"
    elif language == "russian":
        lang_code = "ru"
    elif language == "korean":
        lang_code = "ko"
    elif language == "arabic":
        lang_code = "ar"
    elif language == "japanese":
        lang_code = "ja"
    elif language == "italian":
        lang_code = "it"
    return lang_code