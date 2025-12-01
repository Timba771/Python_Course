
sound_dic = {}

def transcribe_file(path: str, model: str = "tiny") -> dict:

    text = ""
    segments = []
    language = "de"

    return {"text": text, 
            "segments": segments, 
            "language": language 
            }

