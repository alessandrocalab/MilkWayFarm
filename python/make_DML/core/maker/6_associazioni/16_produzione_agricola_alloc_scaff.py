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


#PRODUZIONE_AGRICOLA_ALLOC_SCAFF:DATA_PRODUZIONE_AGRICOLA DATA_INIZIO_CICLO_COLTIVAZIONE CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA NOME_PRODOTTO NUMERO_SCAFFALE CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF QUANTITA_ALLOCATA 

RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE = [
    # GRANO DURO - ambiente secco controllato
    ("DATE '2023-12-28'", "DATE '2023-07-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Grano duro'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 8.40),

    # SEMI GRANO - conservazione semi lungo termine
    ("DATE '2023-12-28'", "DATE '2023-07-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Semi di grano duro'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.80),

    # POMODORO - conservazione verdure fresche
    ("DATE '2024-05-30'", "DATE '2024-03-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Pomodoro'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", 18.00),

    # SEMI POMODORO
    ("DATE '2024-05-30'", "DATE '2024-03-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Semi di pomodoro'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.10),

    # MAIS
    ("DATE '2025-09-29'", "DATE '2025-06-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 14.00),

    # SEMI MAIS
    ("DATE '2025-09-29'", "DATE '2025-06-01'", "'000A'", "'A00A'", "'Struttura Agricola'", "'Semi di mais'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 1.00),

    # MAIS
    ("DATE '2023-11-02'", "DATE '2023-07-05'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 17.50),

    # SEMI MAIS
    ("DATE '2023-11-02'", "DATE '2023-07-05'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Semi di mais'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 1.20),

    # SOIA
    ("DATE '2024-05-14'", "DATE '2024-01-15'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Soia'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 8.75),

    # SEMI SOIA
    ("DATE '2024-05-14'", "DATE '2024-01-15'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Semi di soia'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.80),

    # LATTUGA
    ("DATE '2025-02-24'", "DATE '2025-01-10'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Lattuga'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", 7.00),

    # SEMI LATTUGA
    ("DATE '2025-02-24'", "DATE '2025-01-10'", "'000B'", "'A00A'", "'Struttura Agricola'", "'Semi di lattuga'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.05),

    # POMODORO
    ("DATE '2023-10-27'", "DATE '2023-08-01'", "'000C'", "'A00B'", "'Struttura Agricola'", "'Pomodoro'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", 21.00),

    # SEMI POMODORO
    ("DATE '2023-10-27'", "DATE '2023-08-01'", "'000C'", "'A00B'", "'Struttura Agricola'", "'Semi di pomodoro'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.12),

    # FAGIOLO
    ("DATE '2024-06-28'", "DATE '2024-04-01'", "'000C'", "'A00B'", "'Struttura Agricola'", "'Fagiolo'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", 5.00),

    # SEMI FAGIOLO
    ("DATE '2024-06-28'", "DATE '2024-04-01'", "'000C'", "'A00B'", "'Struttura Agricola'", "'Semi di fagiolo'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.45),

    # PATATA - tuberi e radici
    ("DATE '2023-10-18'", "DATE '2023-07-10'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Patata'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", 6.00),

    # TALEE PATATA
    ("DATE '2023-10-18'", "DATE '2023-07-10'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Talee di patata'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", 0.70),

    # CAROTA - tuberi e radici
    ("DATE '2024-04-21'", "DATE '2024-02-01'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Carota'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", 12.00),

    # SEMI CAROTA
    ("DATE '2024-04-21'", "DATE '2024-02-01'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Semi di carota'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.08),

    # ZUCCHINA
    ("DATE '2025-07-04'", "DATE '2025-05-10'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Zucchina'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", 12.00),

    # SEMI ZUCCHINA
    ("DATE '2025-07-04'", "DATE '2025-05-10'", "'000D'", "'A00C'", "'Struttura Agricola'", "'Semi di zucchina'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 0.10),

    # LATTUGA - produzione recente
    ("DATE '2026-05-20'", "DATE '2026-04-05'", "'001A'", "'A00A'", "'Struttura Agricola II'", "'Lattuga'", "'0002'", "'A00I'", "'Struttura Stoccaggio'", 10.50),

    # SEMI LATTUGA
    ("DATE '2026-05-20'", "DATE '2026-04-05'", "'001A'", "'A00A'", "'Struttura Agricola II'", "'Semi di lattuga'", "'0002'", "'A00G'", "'Struttura Stoccaggio'", 0.07)
]

DATA_PRODUZIONE_AGRICOLA = [riga[0] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

DATA_INIZIO_CICLO_COLTIVAZIONE = [riga[1] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

CODICE_CELLA_IDR = [riga[2] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

CODICE_AREA_CELLA = [riga[3] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

NOME_STRUTTURA_CELLA = [riga[4] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

NOME_PRODOTTO = [riga[5] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

NUMERO_SCAFFALE = [riga[6] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

CODICE_AREA_SCAFF = [riga[7] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

NOME_STRUTTURA_SCAFF = [riga[8] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]

QUANTITA_ALLOCATA = [riga[9] for riga in RIGHE_ALLOC_PRODUZIONE_AGRICOLA_SCAFFALE]


theList=list(zip(DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA))

keys = ["DATA_PRODUZIONE_AGRICOLA", "DATA_INIZIO_CICLO_COLTIVAZIONE", "CODICE_CELLA_IDR", "CODICE_AREA_CELLA", "NOME_STRUTTURA_CELLA", "NOME_PRODOTTO", "NUMERO_SCAFFALE", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_AGRICOLA_ALLOC_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/16_produzione_agricola_alloc_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/16_produzione_agricola_alloc_scaff.sql", lines)