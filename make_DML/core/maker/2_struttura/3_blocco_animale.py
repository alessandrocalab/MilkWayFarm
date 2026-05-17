import os
import sys
import json

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

from make_DML.core.utils.make_DML_line import make_DML_line
from make_DML.core.utils.make_DML import make_DML


#BLOCCO_ANIMALE:NUMERO_BLOCCO NOME_STRUTTURA CODICE_AREA DATA_SMONTAGGIO SUPERFICIE_MQ LIMITE_ALLOCAZIONE DATA_MONTAGGIO 

NUMERO_BLOCCO = [
    "'0001'",
    "'0002'",
    "'0001'",
    "'0002'",
    "'0001'",
    "'0002'",
    "'0003'",
    "'0001'"
]

NOME_STRUTTURA = [
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",
    "'Laboratorio Biologico Delta'"
]

CODICE_AREA = [
    "'AREA-ZOO-01'",
    "'AREA-ZOO-01'",
    "'AREA-ZOO-02'",
    "'AREA-ZOO-02'",
    "'AREA-QUA-01'",
    "'AREA-QUA-01'",
    "'AREA-QUA-01'",
    "'AREA-LAB-02'"
]

DATA_SMONTAGGIO = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

SUPERFICIE_MQ = [
    120,  # Blocco bovini
    95,   # Blocco caprini/ovini
    80,   # Blocco avicoli
    70,   # Blocco piccoli animali
    60,   # Quarantena bovini
    45,   # Quarantena piccoli ruminanti
    35,   # Quarantena avicoli
    40    # Blocco osservazione veterinaria
]

LIMITE_ALLOCAZIONE = [
    12,   # Bovini
    24,   # Caprini/ovini
    80,   # Avicoli
    20,   # Conigli / piccoli animali
    4,    # Quarantena bovini
    8,    # Quarantena piccoli ruminanti
    25,   # Quarantena avicoli
    6     # Osservazione veterinaria
]

DATA_MONTAGGIO = [
    "DATE '2018-10-10'",
    "DATE '2018-10-15'",
    "DATE '2018-11-25'",
    "DATE '2018-12-05'",
    "DATE '2025-03-10'",
    "DATE '2025-03-12'",
    "DATE '2025-03-15'",
    "DATE '2020-04-01'"
]


theList=list(zip(NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, DATA_SMONTAGGIO, SUPERFICIE_MQ, LIMITE_ALLOCAZIONE, DATA_MONTAGGIO))

keys = ["NUMERO_BLOCCO", "NOME_STRUTTURA", "CODICE_AREA", "DATA_SMONTAGGIO", "SUPERFICIE_MQ", "LIMITE_ALLOCAZIONE", "DATA_MONTAGGIO"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, DATA_SMONTAGGIO, SUPERFICIE_MQ, LIMITE_ALLOCAZIONE, DATA_MONTAGGIO\n"
for i in range(len(theList)):
  lines+=make_DML_line("BLOCCO_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/3_blocco_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/3_blocco_animale.sql", lines)