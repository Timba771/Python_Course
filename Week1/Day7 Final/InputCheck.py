"""Sicherer Eingabeprüfer (Basisübung)
Schreibe ein Programm, das:
den Benutzer nach einer Zahl fragt,
prüft, ob sie gültig ist (Fehlerbehandlung mit try/except),
das Quadrat der Zahl ausgibt.
Bonus: Fange zusätzlich den Fall ab, dass die Zahl negativ ist (eigene Fehlermeldung).
🧩 Mini-Check-Prompt:
✅ Wenn dein Programm bei Eingabe von "abc" nicht abstürzt,
und bei -5 eine Warnung ausgibt, bist du auf dem richtigen Weg."""
try: 

    number = input("Enter a number: ")
    if(number.startswith("-")):
        print("Warning number is negativ")
    number = int(number)
    print("Square: ", number**2)


except ValueError:

    print("No real number. Enter a differnt one.")
