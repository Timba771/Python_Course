"""Einkaufslisten-Manager
Funktionen:
Produkt hinzufügen
Produkt löschen
Aktuelle Liste anzeigen
Produkte alphabetisch sortieren
💡 Bonus-Idee:
Wenn du einen Preis mit eingibst (z. B. "Apfel:1.5"), kannst du später die Gesamtsumme berechnen.
→ Vorbereitung auf Dictionaries ({"Apfel": 1.5}) ab Tag 2."""

shopping_list = []
quitting = False

def addProduct(product):
    shopping_list.append(product)

def delProduct(product):
    shopping_list.remove(product)

def showList():
    print(shopping_list)

def sortProducts():
    shopping_list.sort()

def modeSelect(mode):
    global quitting
    match mode:
        case "1":
                addProduct(input("What product would you like to add: "))
        case "2":
                delProduct(input("What product would you like to delete: "))
        case "3":
                showList()
        case "4":
            sortProducts()
            showList()
        case "q": 
            print("Bye")  
            quitting = True

while not quitting :

    modeSelect(str(input("Press: 1-Add Product, 2-Delete Product, 3-ShowList, 4-Sort List, q-quit")))
