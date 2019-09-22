# Kleines Beispiel das zeigt,
# wie man Kommandozeilenparameter in Python ausliest.
#
# Hinweis: um das Skript in PyCharm auszuführen muss
#
# 1. der Python-Interpreter gesetzt werden
#    Um herauszufinden, wo sich der Python-Intrepter
#    der gewünschten Anaconda Umgebung befindet:
#    -> Anaconda Prompt öffnen
#       -> "conda env list" eingeben
#          (Pfade pro Umgebung werden angezeigt,
#           dort liegt das python.exe)
#       oder
#       -> activate <umgebungsname>
#       -> "where python" eingeben
#          (dort liegt das python.exe)
#
# 2. eine Run-Konfiguration erstellt werden

import sys

print("1".isdigit()) # True
print("2.2".isdigit()) # False

print("Hallo! Du hast das Skript mit folgenden Parametern aufgerufen:")

print(type(sys.argv))

summe = 0

for a in sys.argv:
    print(a, type(a))
    if a.isdigit():
        print("Wandle ",a," in eine Zahl um!")
        summe = summe + int(a)

print("Die Summe der Zahlen ist:", summe)
