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


#SENSORE:SERIALE NOME_PRODUTTORE NOME_MODELLO CODICE_AREA NOME_STRUTTURA 

SERIALE = []

NOME_PRODUTTORE = []

NOME_MODELLO = []

CODICE_AREA = []

NOME_STRUTTURA = []


theList=list(zip(SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA))

keys = ["SERIALE", "NOME_PRODUTTORE", "NOME_MODELLO", "CODICE_AREA", "NOME_STRUTTURA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA\n"
for i in range(len(theList)):
  lines+=make_DML_line("SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/7_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/7_sensore.sql", lines)