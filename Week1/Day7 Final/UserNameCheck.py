"""Benutzername-Validator (Fehler + Strings kombiniert)
Schreibe eine Funktion check_username(name), die prüft:
Der Name darf nicht leer sein.
Muss mindestens 3 Zeichen lang sein.
Darf keine Sonderzeichen (außer _) enthalten.
Wenn eine Regel verletzt ist → wirf eine ValueError mit passender Meldung."""

try: 
    while True:

        def check_usernaem(name):
            
            if len(name) < 3:
                print("Name is too short(at leats three)")


        check_usernaem(input("Enter a username: "))

except ValueError: 
    print("No real name enter a differnt one")