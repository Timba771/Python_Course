"""Top-5-Tasks-Liste
Ziel:
Ein Programm, das Aufgaben vom Nutzer entgegennimmt, sortiert und als „Top-5-Liste“ ausgibt.
Anforderungen:
Nutzer gibt beliebig viele Aufgaben ein (Ende mit leerem Eingabefeld).
Liste wird automatisch nach Länge der Aufgabe sortiert.
Ausgabe erfolgt umgekehrt („wichtigste zuerst“).
Ausgabe ist nummeriert (verwende enumerate())."""

tasks = []

while True:
    task = input("Neue Aufgabe (oder leer zum Beenden): ")
    if task == "":
        break
    if task not in tasks:     # Duplikate verhindern
        tasks.append(task)

    tasks.sort(key=len, reverse=True)
    print(task)

    print("\n Top-Tasks:")
    for i, t in enumerate(tasks[:5], start=1):
        print(f"{i}. {t}")


    

