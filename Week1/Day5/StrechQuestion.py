
numbers = input("Enter numbers, seperate with ',' : ")
numbers_list = [ int(number) for number in numbers.split(",")]
even_list =[]

for even in numbers_list:
    if even % 2 == 0:
        even_list.append(even)

for e in sorted(even_list):
    print(e)
#for n in sorted(numbers_list):
    #print(n)