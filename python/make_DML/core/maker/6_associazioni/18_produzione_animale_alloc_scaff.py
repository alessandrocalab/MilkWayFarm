import os
import sys
import json

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

from python.make_DML.core.utils.make_DML_line import make_DML_line
from python.make_DML.core.utils.make_DML import make_DML


#PRODUZIONE_ANIMALE_ALLOC_SCAFF:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA_BLOCCO CODICE_AREA_BLOCCO NOME_PRODOTTO NUMERO_SCAFFALE CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF QUANTITA_ALLOCATA 

RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE = [
    # LETAME BOVINO - biomasse organiche
    ("DATE '2025-02-26'", "'0001'", "'Struttura Zootecnica'", "'A00B'", "'Letame bovino'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 52.04),

    # POLLINA - biomasse organiche
    ("DATE '2025-02-26'", "'0001'", "'Struttura Zootecnica'", "'A00C'", "'Pollina'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 0.07),

    # LETAME OVINO - biomasse organiche
    ("DATE '2025-02-26'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Letame ovino'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 3.34),

    # LETAME BOVINO
    ("DATE '2025-02-27'", "'0001'", "'Struttura Zootecnica'", "'A00B'", "'Letame bovino'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 61.30),

    # POLLINA
    ("DATE '2025-02-27'", "'0001'", "'Struttura Zootecnica'", "'A00C'", "'Pollina'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 0.09),

    # POLLINA
    ("DATE '2025-03-09'", "'0001'", "'Struttura Zootecnica'", "'A00C'", "'Pollina'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 0.12),

    # LETAME OVINO
    ("DATE '2025-03-09'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Letame ovino'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 3.26),

    # LETAME SUINO
    ("DATE '2025-06-18'", "'0003'", "'Struttura Zootecnica'", "'A00B'", "'Letame suino'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 19.97),

    # POLLINA
    ("DATE '2025-06-18'", "'0004'", "'Struttura Zootecnica'", "'A00B'", "'Pollina'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 0.16)
]
DATA_PRODUZIONE = [riga[0] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

NUMERO_BLOCCO = [riga[1] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

NOME_STRUTTURA_BLOCCO = [riga[2] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

CODICE_AREA_BLOCCO = [riga[3] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

NOME_PRODOTTO = [riga[4] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

NUMERO_SCAFFALE = [riga[5] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

CODICE_AREA_SCAFF = [riga[6] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

NOME_STRUTTURA_SCAFF = [riga[7] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

QUANTITA_ALLOCATA = [riga[8] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SCAFFALE]

theList=list(zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA))

keys = ["DATA_PRODUZIONE", "NUMERO_BLOCCO", "NOME_STRUTTURA_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_PRODOTTO", "NUMERO_SCAFFALE", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_ANIMALE_ALLOC_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/18_produzione_animale_alloc_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/18_produzione_animale_alloc_scaff.sql", lines)