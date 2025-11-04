def question(number):
    if number > 10:
        print("Größer als 10? True")
    else:
        print("Größer als 10? False")

    if number % 2 == 0:
        print("Gerade? True")
    else:
        print("Gerade? False")

    if 5 <= number <= 20:  # inklusiv
        print("Zwischen 5 und 20? True")
    else:
        print("Zwischen 5 und 20? False")

question(int(input("Gib eine Nummer an: ")))