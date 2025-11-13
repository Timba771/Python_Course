import json
import os

recipes_file  = "recipes.json"   # nicht recepies
ideas_file    = "ideas.json"
projects_file = "projects.json"

def loadData(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # leere/kaputte Datei -> als leeres Dict behandeln
            return {}
    return {}

def saveData(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def fileCreation(filename):
    return loadData(filename)   # <-- Ergebnis zurückgeben


def fileManipulation(data, filename):
    action = input("New (n) | Show (s) | Del (d) | Back (b): ").strip().lower()
    match action:
        case "n":
            # hier: key/value erfragen, in 'data' eintragen
            # danach:
            saveData(filename, data)
        case "s":
            # hier: 'data' hübsch ausgeben
            pass
        case "d":
            # key erfragen, falls vorhanden: del data[key]
            # danach:
            saveData(filename, data)
        case "b":
            return  # zurück zum Kategorien-Menü
        case _:
            print("Unknown option.")


while True:
    opt = input("Which category? (1.recipes, 2.ideas, 3.projects, q.quit): ").strip().lower()
    if opt == "q":
        break

    if opt == "1":
        current_file = recipes_file
    elif opt == "2":
        current_file = ideas_file
    elif opt == "3":
        current_file = projects_file
    else:
        print("Invalid.")
        continue

    # Daten laden und im RAM halten
    current_data = loadData(current_file)

    # Inneres Menü für diese Kategorie (bleibt hier, bis Nutzer 'b' drückt)
    while True:
        back = fileManipulation(current_data, current_file)
        if back is not None:  # z.B. return von 'b'
            break