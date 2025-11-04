used = 0
userIn = ""
while userIn != "q":
    used += 1
    print(used) 
    print("-------- Mini-Menue----------")
    print("1 - Zinsrechner starten")
    print("2 - Temp-Um Starten")
    print("3 - Mini-Quiz starten")
    print("q - beenden")

    userIn = input("Wähle eine option: ")

    if (userIn == "1"):
        print(" Zinsrechner ausgewählt")

    elif(userIn == "2"):
        print(" TEmp-Um ausgewählt")

    elif(userIn == "3"):
        print("Mini-Quiz ausgewählt")

    elif(userIn == "q"):
        print("Tschüss")
    else: 
        print("Bitte wählen sie etwas anderes")
p