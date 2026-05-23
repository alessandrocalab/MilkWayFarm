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


#REGISTRAZIONE_SENSORE:SERIALE DATA_SECONDI NOME_PRODUTTORE MISURAZIONE 

SERIALE = []

DATA_SECONDI = []

NOME_PRODUTTORE = []

MISURAZIONE = []


theList=list(zip(SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE))

keys = ["SERIALE", "DATA_SECONDI", "NOME_PRODUTTORE", "MISURAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("REGISTRAZIONE_SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/8_registrazione_sensore.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/8_registrazione_sensore.sql.bak", lines)