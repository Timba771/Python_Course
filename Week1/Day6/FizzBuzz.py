number_list = [int(i) for i in range(1,31)]
print(number_list)
tag_list = []

for n in number_list:
    if (n % 3 == 0) and (n % 5 == 0):
        tag_list.append(str(n))
        tag_list.append("FizzBuzz")
        
    elif n % 3 == 0:
        tag_list.append(str(n))
        tag_list.append("Fizz")
        
    elif n % 5 == 0:
        tag_list.append(str(n))
        tag_list.append("Buzz")
    else:
        tag_list.append(str(n))

print(tag_list)