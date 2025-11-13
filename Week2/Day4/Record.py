import sounddevice as sd
import numpy as np
import os
import soundfile as sf

sound_list = []
seconds_recoring = 10.0


def show_menu():
    print("What do you want to do? ")
    
    print("1) record") 
    print("2) play")
    print("3) quit")
    option = int(input("enter number here: ").strip())
    if option == 1 or option == 2 or option == 3:
        print("Option", option, "has been choosen.")
        return option
    else:
        print("[Enter a valid option]")

def record_sound(seconds: float, sampelrate: int = 16000, channels: int = 1, dtype: str = "float32", device: int | None = None) -> "np.ndarry":
    
    #Error Handling
    if seconds <= 0:
        ValueError
    if sampelrate <= 0:
        ValueError
    if channels not in {1,2}:
        ValueError
    if dtype != "float32":
        ValueError 

    #Frame callucaltion
    frames = int(seconds * sampelrate)

    # erzeugt array
    audio = sd.rec(frames, samplerate= sampelrate, channels=channels)

    sd.wait()
    print(audio.shape)

    if audio.ndim != 2:
        raise RuntimeError("Audio must be 2-dimensional ")

    return audio , sampelrate
    #sound_list.append(name)

def save_wave(path, audio, samplerate):
    if audio.ndim != 2:
        raise RuntimeError("Audio must be 2-dimensional ")
    if samplerate <= 0:
        raise RuntimeError("SampleRate must be over 0 ")
    if os.path.exists(path):
        raise FileExistsError("Fille Already Exists")
    
    sf.write(path, audio, samplerate)



def play_sound(audio ,samplerate):
    print("palysound")

    sd.play(name)

def main():
    print("Hello User:")
    while True:
        try:
            option = show_menu()
            match option:

                #Recording Sound
                case 1:

                    name = input("Enter a name: ")
                    audio, samplerate = record_sound(seconds_recoring)
                    save_wave(f"{name}.wav", audio, samplerate)
                #Playing sound
                case 2:

                    print("Choose a sound")
                    print(sound_list)
                    chosen = input("Enter name here:")
                    play_sound(name)

                #Quit
                case 3:
                    print("bye")
                    break
        except ValueError:
            print("Bad value!")
if __name__ == "__main__":
    main()
