from stt_backend import transcribe_file


def main():
    name = input("Enter filename: ")
    #dict_dict = {}
    result = transcribe_file(f"{name}.wav")
    print("Full text: ")
    print(result["text"])

    print("Language: ")
    print(result["language"])

    print("Segments:")
    for seg in result["segments"]:
        start = seg["start"]
        end = seg["end"]
        text = seg["text"]
        print(f"[{start:.2f}s - {end:.2f}s] {text}")

if __name__ == "__main__":
    main()