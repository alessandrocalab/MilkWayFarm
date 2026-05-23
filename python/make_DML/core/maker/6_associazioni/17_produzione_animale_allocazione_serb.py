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


#PRODUZIONE_ANIMALE_ALLOC_SERB:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA_BLOCCO CODICE_AREA_BLOCCO NOME_PRODOTTO NUMERO_SERBATOIO CODICE_AREA_SERB NOME_STRUTTURA_SERB QUANTITA_ALLOCATA 

RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO = [
    # LATTE CAPRINO
    ("DATE '2025-02-24'", "'0001'", "'Struttura Zootecnica'", "'A00A'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 1.80),
    ("DATE '2025-02-25'", "'0001'", "'Struttura Zootecnica'", "'A00A'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 2.02),
    ("DATE '2025-02-26'", "'0001'", "'Struttura Zootecnica'", "'A00A'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 2.47),

    # LATTE BOVINO
    ("DATE '2025-02-26'", "'0001'", "'Struttura Zootecnica'", "'A00B'", "'Latte bovino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 48.40),

    # LATTE CAPRINO / OVINO
    ("DATE '2025-02-26'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 5.27),
    ("DATE '2025-02-26'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Latte ovino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 3.03),

    # LATTE CAPRINO / BOVINO
    ("DATE '2025-02-27'", "'0001'", "'Struttura Zootecnica'", "'A00A'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 3.21),
    ("DATE '2025-02-27'", "'0001'", "'Struttura Zootecnica'", "'A00B'", "'Latte bovino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 42.97),

    # LATTE CAPRINO
    ("DATE '2025-02-27'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 4.46),

    # LATTE CAPRINO / OVINO
    ("DATE '2025-03-09'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Latte caprino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 4.69),
    ("DATE '2025-03-09'", "'0002'", "'Struttura Zootecnica'", "'A00B'", "'Latte ovino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 2.95),

    # LATTE OVINO
    ("DATE '2025-03-09'", "'0002'", "'Struttura Zootecnica'", "'A00C'", "'Latte ovino'", "'S001'", "'A00C'", "'Struttura Stoccaggio'", 0.91)
]
DATA_PRODUZIONE = [riga[0] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

NUMERO_BLOCCO = [riga[1] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

NOME_STRUTTURA_BLOCCO = [riga[2] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

CODICE_AREA_BLOCCO = [riga[3] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

NOME_PRODOTTO = [riga[4] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

NUMERO_SERBATOIO = [riga[5] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

CODICE_AREA_SERB = [riga[6] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

NOME_STRUTTURA_SERB = [riga[7] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

QUANTITA_ALLOCATA = [riga[8] for riga in RIGHE_ALLOC_PRODUZIONE_ANIMALE_SERBATOIO]

theList=list(zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA))

keys = ["DATA_PRODUZIONE", "NUMERO_BLOCCO", "NOME_STRUTTURA_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_PRODOTTO", "NUMERO_SERBATOIO", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_ANIMALE_ALLOC_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/17_produzione_animale_allocazione_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/17_produzione_animale_allocazione_serb.sql", lines)