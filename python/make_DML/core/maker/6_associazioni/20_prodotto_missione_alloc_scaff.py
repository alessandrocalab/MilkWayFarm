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


#PRODOTTO_MISSIONE_ALLOC_SCAFF:NOME_PRODOTTO NOME_MISSIONE NUMERO_SCAFFALE CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF QUANTITA_ALLOCATA 
RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE = [
    # ARES SUPPLY 01 - SEMI
    ("'Semi di grano duro'", "'Ares Supply 01'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 40.00),
    ("'Semi di mais'", "'Ares Supply 01'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 35.00),

    # ARES SUPPLY 02 - MANGIMI
    ("'Mangime bovini crescita'", "'Ares Supply 02'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", 750.00),
    ("'Mangime pollame ovaiole'", "'Ares Supply 02'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", 300.00),

    # DEMETRA CARGO 01 - MATERIALE AGRICOLO SECCO
    ("'Lana di roccia agricola'", "'Demetra Cargo 01'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", 250.00),

    # DEMETRA CARGO 02 - SEMI
    ("'Semi di pomodoro'", "'Demetra Cargo 02'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 8.00),
    ("'Semi di lattuga'", "'Demetra Cargo 02'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 5.00),

    # HERMES BIOLAB 01 - PRODOTTO SANITARIO NON LIQUIDO
    ("'Antibiotico veterinario pollame'", "'Hermes BioLab 01'", "'0001'", "'A00E'", "'Struttura Stoccaggio'", 250.00),

    # HERMES BIOLAB 02 - MANGIMI / PRODOTTO SANITARIO SOLIDO
    ("'Mangime ovicaprini'", "'Hermes BioLab 02'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", 500.00),
    ("'Mangime suini'", "'Hermes BioLab 02'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", 600.00),
    ("'Reidratante orale veterinario'", "'Hermes BioLab 02'", "'0001'", "'A00E'", "'Struttura Stoccaggio'", 80.00),

    # ATLAS STORAGE 01 - BIOMASSE / MANGIMI SECCHI
    ("'Compost sterile'", "'Atlas Storage 01'", "'0001'", "'A00K'", "'Struttura Stoccaggio'", 600.00),
    ("'Fieno essiccato'", "'Atlas Storage 01'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 900.00),
    ("'Paglia'", "'Atlas Storage 01'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", 700.00),

    # ATLAS STORAGE 02 - SEMI
    ("'Semi di carota'", "'Atlas Storage 02'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 6.00),
    ("'Semi di zucchina'", "'Atlas Storage 02'", "'0001'", "'A00G'", "'Struttura Stoccaggio'", 5.00)
]
NOME_PRODOTTO = [riga[0] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]

NOME_MISSIONE = [riga[1] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]

NUMERO_SCAFFALE = [riga[2] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]

CODICE_AREA_SCAFF = [riga[3] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]

NOME_STRUTTURA_SCAFF = [riga[4] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]

QUANTITA_ALLOCATA = [riga[5] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SCAFFALE]
theList=list(zip(NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA))

keys = ["NOME_PRODOTTO", "NOME_MISSIONE", "NUMERO_SCAFFALE", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_MISSIONE_ALLOC_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/20_prodotto_missione_alloc_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/20_prodotto_missione_alloc_scaff.sql", lines)