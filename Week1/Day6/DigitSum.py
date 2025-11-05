
summe = 0
number_list =[]
numbers = input("Enter Numbers: ")
for ziffer in str(numbers):
    number_list.append(int(ziffer))
    summe += int(ziffer)
print(numbers)
print(" + ".join(str(i) for i in number_list), " = ", summe)