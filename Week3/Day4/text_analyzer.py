 
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_DIR = BASE_DIR / "texts"

def read_file(file_path)-> str:
    #text = ""
    if file_path.exists() and file_path.is_dir():
      
        print("Folder Found")
        print(f"The folder is {file_path}")
        
        for files in  file_path.iterdir():
            if files.is_file() and files.suffix == ".txt":
                print(f"textFileFound: {files.name}")
                with open(files) as f:
                    return str(f.read())


def workable_text(text):
    lower_text = text.lower()
    no_punctuation_text = lower_text.replace(",", " " ).replace(";", " " ).replace(".", " " ) .replace(":", " " ).replace("?", " " ).replace("!", " " )
    
    # change Text into list 
    word_list = []
    for words in no_punctuation_text.split(" "):
        word_list.append(words)
    return word_list

def word_count(word_list):
    word_count_dict = {}
    for word in word_list:
        if word == " " or word == "":
            #dont use 
            pass
        elif word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    return(word_count_dict)

def print_dict(word_dict):
    sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
    for elements in list(sorted_dict)[:10]:
        print(elements, "  ",sorted_dict[elements])

def main():
    text = read_file(FILE_DIR)
    workable_word_list = workable_text(text)
    word_count_dictonary = word_count(workable_word_list)
    print_dict(word_count_dictonary)

if __name__ == "__main__":
    main()