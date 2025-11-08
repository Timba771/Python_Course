
import json
quit = False
data_name = ""
direct ={}

def newCreate(name):
    direct[name]= str(input("Entry: "))
    with open("data.json", "w") as f:
        json.dump(direct, f, indent = 4)
def show_Created():
    with open("data.json", "r") as f:
        data = json.load(f)
        print(data)

def search_by_key():
    search_key = input("What key would you like to search?")
    if search_key in direct:
        print(direct[search_key], " was found")
    else:
        print("Key is not in list! ")
        search_by_key()
    keyoptions(search_key)

def keyoptions(my_key):
    options = input("Delet keyvalue pair? (y/n)")
    if options == "y":
        if my_key in direct:
            direct.pop(my_key)

        with open("data.json", "w") as f:
            json.dump(direct, f, indent=4)
            print(f"Deleted: {my_key}")

    elif options == "n":
        print("Returing to Menue...")
    else:
        print()

while quit == False:
    selection = input("New (n), Show(s), Quit (q): ").strip().lower()
    #print(direct)

    match selection:
        case "n":
            name = input("give a name: ")
            newCreate(name)
        case "s":
            what_to_show = input("Whole Direct? (Y/N)").strip().lower()
            if what_to_show == "y":
                
                show_Created()
            elif what_to_show== "n":
                search_by_key()
            else:
                print("Enter something different")
        case "q":
            quit = True
            print("Bye")
        case _:
            print("Wrong Input")

