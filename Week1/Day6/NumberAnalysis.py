
numbers = [int (n) for n in input("Enter Numbers, seperate with ',' : ").split(",")]
even_list = []
odd_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.append(number)
    else: 
        odd_list.append(number)

print(f"Even: {sorted(even_list)}")
print(f"Odd: {sorted(odd_list)}")

print(f"Sum of all numbers: {sum(numbers)}")
print(f"Biggest odd Value: {max(odd_list)}")