
from gtts import gTTS
import GenerateMp3
import PlayMp3

text_user_select = "Choose one option: "

#Shows Menue
def show_menu():
    print("----------")
    print("1) Put in Text (i) ")
    print("2) Play file (p)")
    print("3) Quit (q)")

#user selction
def user_select(text):
    selection = input(text).strip().lower()
    match selection: 
        case "i":
            return selection
        case "p":
            return selection
        case "q":
            return selection
        case None:
            return ""
        
#def put_in_text():
    


def main():
    print("Voice Assitent started...")

    #loop
    while True:
        
        show_menu()
        choice = user_select(text_user_select)
        
        match choice:
            case "i":
               print("Option 1 has been choosen")
               text = input("What text would you like to generate: ")
               name = input("Enter a name: ")
               file_name = GenerateMp3.text_to_mp3(text, f"{name}.mp3", "en")
               print(file_name, "has been generated")
               print("Talking starting...")
               PlayMp3.play_file(file_name)
               
            case "p":
                format = ".mp3"
                print("Option 2 has been choosen")
                file_name = input("enter the name(.mp3)").strip()
                if not file_name.endswith(format):
                    file_name += format
                PlayMp3.play_file(file_name)
            case "q":
                print("bye")
                break

if __name__ == "__main__":
    main()