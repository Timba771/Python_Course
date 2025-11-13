# Erstelle eine Liste mit deinen Lieblingszahlen
# a) Füge eine neue Zahl hinzu
# b) Füge an Position 2 eine Zahl ein
# c) Entferne eine bestimmte Zahl
# d) Sortiere die Liste und drehe sie um
# e) Zähle, wie oft eine Zahl vorkommt
# f) Gib den Index einer bestimmten Zahl aus

liste = [7, 14, 28, 45, 21,14]

liste.append(22)
liste.insert(33,2)
liste.remove(7)
print(liste.index(45))
liste.sort(reverse=True)
print(liste.count(14))
print(liste.index(45))
print(liste)

if 22 in liste:
    print("22 is here: ",liste.index(22) )
