"""Baue eine Zahlerraten-App, die:
eine zufällige Zahl zwischen 1–100 generiert (import random)
den Benutzer raten lässt,
nach jedem Versuch Feedback gibt („zu hoch“, „zu niedrig“)
und mitzählt, wie viele Versuche gebraucht wurden."""

import random
tries = 6
user_guess_count = 0
print("Random number has been generated....")
number = round(random.uniform(1,100))
while True:
    print("You have ", tries - user_guess_count, " left!")
    user_input = input("Enter your guess: ")
    user_guess_count += 1
    
    user_input = int(user_input)
    if user_guess_count == tries:
        print("too many tries")
        break

    if user_input == number:
        print("Your guess was right")
        break
    elif user_input > number:
        print("Number is too high")
    elif user_input < number:
        print("Number is too low")
    else:
        print("Enter a number between 1 an 100")

print(number, " is the right one")