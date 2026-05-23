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


#SCAFFALE:NUMERO_SCAFFALE CODICE_AREA NOME_STRUTTURA DATA_SMONTAGGIO DATA_MONTAGGIO CAPACITA_KG DIMENSIONE_M3 

NUMERO_SCAFFALE = []

CODICE_AREA = []

NOME_STRUTTURA = []

DATA_SMONTAGGIO = []

DATA_MONTAGGIO = []

CAPACITA_KG = []

DIMENSIONE_M3 = []


theList=list(zip(NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3))

keys = ["NUMERO_SCAFFALE", "CODICE_AREA", "NOME_STRUTTURA", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "CAPACITA_KG", "DIMENSIONE_M3"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3\n"
for i in range(len(theList)):
  lines+=make_DML_line("SCAFFALE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/4_scaffale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/4_scaffale.sql", lines)