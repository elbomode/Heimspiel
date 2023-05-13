import Funktionen
from pathlib import Path

with open('Heimspiel.ini') as file:
    lines = [line.rstrip() for line in file]

path = Path("E:\Projekte\Testdaten")
debug = False

Funktionen.Altersklassen(lines,path)
Funktionen.Wettbewerbsliste(lines,path)