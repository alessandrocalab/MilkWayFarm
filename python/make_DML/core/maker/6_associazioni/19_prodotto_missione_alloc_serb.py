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


#PRODOTTO_MISSIONE_ALLOC_SERB:NOME_PRODOTTO NOME_MISSIONE NUMERO_SERBATOIO CODICE_AREA_SERB NOME_STRUTTURA_SERB QUANTITA_ALLOCATA 
RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO = [
    # ARES SUPPLY 01 - liquidi agricoli / acqua
    ("'Acqua potabile'", "'Ares Supply 01'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 1200.00),
    ("'Soluzione nutritiva idroponica base'", "'Ares Supply 01'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 500.00),

    # ARES SUPPLY 02
    ("'Acqua potabile'", "'Ares Supply 02'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 1500.00),

    # prodotto sanitario liquido
    ("'Antiparassitario bovini'", "'Ares Supply 02'", "'S003'", "'A00E'", "'Struttura Stoccaggio'", 65.00),

    # DEMETRA CARGO 01
    ("'Biofertilizzante microbico'", "'Demetra Cargo 01'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 180.00),

    # DEMETRA CARGO 02
    ("'Acqua potabile'", "'Demetra Cargo 02'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 1000.00),
    ("'Soluzione nutritiva concentrata'", "'Demetra Cargo 02'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", 350.00),

    # HERMES BIOLAB 01 - liquidi sanitari
    ("'Vaccino bovini respiratorio'", "'Hermes BioLab 01'", "'S003'", "'A00E'", "'Struttura Stoccaggio'", 180.00),
    ("'Vaccino pollame Newcastle'", "'Hermes BioLab 01'", "'S003'", "'A00E'", "'Struttura Stoccaggio'", 90.00),

    # ATLAS STORAGE 01
    ("'Acqua potabile'", "'Atlas Storage 01'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", 1800.00),

    # ATLAS STORAGE 02
    ("'Acqua potabile'", "'Atlas Storage 02'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", 1500.00),
    ("'Correttore pH acido'", "'Atlas Storage 02'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", 120.00),
    ("'Correttore pH basico'", "'Atlas Storage 02'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", 100.00)
]
NOME_PRODOTTO = [riga[0] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]

NOME_MISSIONE = [riga[1] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]

NUMERO_SERBATOIO = [riga[2] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]

CODICE_AREA_SERB = [riga[3] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]

NOME_STRUTTURA_SERB = [riga[4] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]

QUANTITA_ALLOCATA = [riga[5] for riga in RIGHE_ALLOC_PRODOTTO_MISSIONE_SERBATOIO]
theList=list(zip(NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA))

keys = ["NOME_PRODOTTO", "NOME_MISSIONE", "NUMERO_SERBATOIO", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_MISSIONE_ALLOC_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/19_prodotto_missione_alloc_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/19_prodotto_missione_alloc_serb.sql", lines)