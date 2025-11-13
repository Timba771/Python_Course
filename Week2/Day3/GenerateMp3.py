
from gtts import gTTS

def text_to_mp3(text: str, name: str , lang: str ) -> str:
    tts = gTTS(text = text, lang = lang)
    tts.save(name)
    return name