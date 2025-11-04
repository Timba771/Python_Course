
eingabe = input("Enter five Temperatures in C ")
all_fahrenheit = []
avgfar = 0
avgcel = 0

temperatures = [float(t) for t in eingabe.split(",")]

print("Temperatur-Umrechner")
print("--------------------")
print("Entry", eingabe )
for celcius in temperatures:
    farenheit = celcius * 9 / 5 + 32
    print(celcius, "C =  ", round(farenheit,1),"F\n")
    all_fahrenheit.append(farenheit)
    avgcel += celcius

for far in all_fahrenheit:
    avgfar += far
avgfar = avgfar / len(all_fahrenheit)
avgcel = avgcel / len(temperatures)
print("avg:", avgcel,"   ", avgfar)