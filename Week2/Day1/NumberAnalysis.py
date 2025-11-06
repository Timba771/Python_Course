"""Zahlenanalyse
Erstelle eine Liste mit beliebigen 10 Ganzzahlen.
Berechne:
Summe (sum())
Durchschnitt (sum()/len())
größte & kleinste Zahl (max(), min())
Gib die Ergebnisse formatiert aus."""

liste = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(sum(liste))

print(sum(liste)/len(liste))

print(min(liste), max(liste))