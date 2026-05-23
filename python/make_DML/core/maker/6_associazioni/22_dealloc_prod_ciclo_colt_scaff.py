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


#DEALLOC_PROD_CICLO_COLT_SCAFF:DATE_MIN NOME_PRODOTTO NUMERO_SCAFF CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA QUANTITA_DEALLOCATA 

RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE = [
    # CICLO LATTUGA - 2025-01-10
    # Semi di lattuga arrivati con Demetra Cargo 02, allocati in A00G
    ("DATE '2024-06-17'", "'Semi di lattuga'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", "DATE '2025-01-10'", "'000B'", "'A00A'", "'Struttura Agricola'", 0.20),

    # CICLO MAIS - 2025-06-01
    # Semi di mais arrivati con Ares Supply 01
    ("DATE '2023-05-12'", "'Semi di mais'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", "DATE '2025-06-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 0.40),

    # CICLO PATATA - 2026-04-04
    # Talee prodotte dal ciclo precedente e allocate in A00H
    ("DATE '2023-10-18'", "'Talee di patata'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", "DATE '2026-04-04'", "'001C'", "'A00A'", "'Struttura Agricola II'", 0.20),

    # CICLO LATTUGA - 2026-04-05
    ("DATE '2024-06-17'", "'Semi di lattuga'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001A'", "'A00A'", "'Struttura Agricola II'", 0.30),

    # CICLO MAIS - 2026-04-05
    ("DATE '2023-05-12'", "'Semi di mais'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001B'", "'A00A'", "'Struttura Agricola II'", 0.50),

    # CICLO FAGIOLO - 2026-05-21
    # Semi di fagiolo prodotti dal ciclo 2024-04-01 / 2024-06-28
    ("DATE '2024-06-28'", "'Semi di fagiolo'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", "DATE '2026-05-21'", "'001A'", "'A00A'", "'Struttura Agricola II'", 0.30)
]
DATE_MIN = [riga[0] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

NOME_PRODOTTO = [riga[1] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

NUMERO_SCAFF = [riga[2] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

CODICE_AREA_SCAFF = [riga[3] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

NOME_STRUTTURA_SCAFF = [riga[4] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

DATA_INIZIO = [riga[5] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

CODICE_CELLA_IDR = [riga[6] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

CODICE_AREA_CELLA = [riga[7] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

NOME_STRUTTURA_CELLA = [riga[8] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

QUANTITA_DEALLOCATA = [riga[9] for riga in RIGHE_DEALLOC_SCAFFALE_CICLO_COLTIVAZIONE]

theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SCAFF", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "DATA_INIZIO", "CODICE_CELLA_IDR", "CODICE_AREA_CELLA", "NOME_STRUTTURA_CELLA", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_CICLO_COLT_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/22_dealloc_prod_ciclo_colt_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/22_dealloc_prod_ciclo_colt_scaff.sql", lines)