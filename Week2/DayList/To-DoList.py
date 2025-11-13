""""Kleine To-Do-Liste
Erstelle eine leere Liste todos = [].
Lass den Nutzer über input() 3 Aufgaben eingeben.
Füge sie jeweils der Liste hinzu.
Gib die komplette Liste aus.
Entferne eine erledigte Aufgabe über den Namen."""

todos = []
while True:
    user = input("what do you want to do ? = > new Entry ('n'), delete Entry ('d'), quit (q)")
    print(todos)
    match user:

        case "n":
            raw = input(" Enter some entrys(part by ,) ")
            entries = [e.strip() for e in raw.split(",") if e.strip()]

            new_item = [e for e in entries if e not in todos]

        case "d":
            remove = input("what do you want to remove? ")
            todos.remove(remove)
        case "q":
            print("ok bye")
            break
    
    