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

NUMERO_BLOCCO = []

NOME_STRUTTURA = []

CODICE_AREA = []

DATA_SMONTAGGIO = []

SUPERFICIE_MQ = []

LIMITE_ALLOCAZIONE = []

DATA_MONTAGGIO = []


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