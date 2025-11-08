"""Grundoperationen
Erstelle ein Dictionary mit Notizen:
notes = {
    "2025-11-07": "Learn JSON basics",
    "2025-11-08": "Try APIs with requests"
}
Speichere es mit json.dump() in notes.json.
Lade es wieder ein und gib es aus.
Ergänze ein weiteres Element und speichere erneut.
💡 Tipp: Verwende indent=4 in json.dump(), um die Datei schön lesbar zu machen."""


import json

notes = {
    "2025-11-07": "Learn JSON Basicc",
    "2025-11-08": "Try APIs with request"
}

with open("data.json", "w") as jsonBasics:
    json.dump(notes,jsonBasics)

with open("data.json", "r") as jsonBasics:
    print(json.load(jsonBasics), "OUTPUT")

key, value = input("Enter a key and a value (seperate with ,): ").split(",")

notes[key] = value

with open("data.json", "w") as jsonBasics:
    json.dump(notes,jsonBasics,indent=4)

with open("data.json", "r") as jsonBasics:
    print(json.load(jsonBasics), "OUTPUT2")