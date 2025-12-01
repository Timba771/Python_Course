import secrets
import random 

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!$%&?@#*"


def user_input()->int:
    print(" -------------------------------------------- ")
    print("              Password-Generator              ")
    print(" -------------------------------------------- ")
    length = int(input(".  How long should the password be?    "))
    print(" -------------------------------------------- ")
    return length


def build_charset()-> str:
    char_set = lowercase_letters + uppercase_letters + digits + symbols
    return char_set


def genrator(length, char_set)-> str:
    password = ""

    # mus be conditions
    password += secrets.choice(uppercase_letters)
    password += secrets.choice(digits)
    password += secrets.choice(symbols)

    # rest random
    for i in range(length-3):
        password += secrets.choice(char_set)
    return password


def ranomize_password(password)-> str:
    password_list = []
    password_string = ""
    for i in range(len(password)):
        password_list.append(password[i])
    
    random.shuffle(password_list)

    for j in password_list:
        password_string += j

    return password_string


def print_out(final_password):
    print("Password has been generated")
    print(f"Your password is: {final_password}")

def main():
    char_set = build_charset()
    length = user_input()
    password = genrator(length, char_set)
    randomized_password = ranomize_password(password)
    print_out(randomized_password)


if __name__ == "__main__":
    main()