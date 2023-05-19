import Funktionen
from pathlib import Path
import pandas as pd

with open('Heimspiel.ini') as file:
    lines = [line.rstrip() for line in file]

# path = Path("E:\Projekte\Testdaten")
path = Path(r"\\s04bi-store\PROD_BACKUP_01\11 Extraktion\Heimspiel")
debug = False

# Funktionen.Altersklassen(lines,path)
# Funktionen.Wettbewerbsliste(lines,path)
# Funktionen.Länderliste(lines,path)
# Funktionen.Eventtypen(lines,path)
# Funktionen.SaisonsProWettbewerb(lines,path)
Funktionen.SpielplanProSaison(lines,path)