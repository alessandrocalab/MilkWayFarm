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


#CELLA_IDROPONICA:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA SISTEMA_IDROPONICO DATA_SMONTAGGIO DATA_MONTAGGIO MAX_COLTURE 

CODICE_CELLA_IDR = []

CODICE_AREA = []

NOME_STRUTTURA = []

SISTEMA_IDROPONICO = []

DATA_SMONTAGGIO = []

DATA_MONTAGGIO = []

MAX_COLTURE = []


theList=list(zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE))

keys = ["CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "SISTEMA_IDROPONICO", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "MAX_COLTURE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE\n"
for i in range(len(theList)):
  lines+=make_DML_line("CELLA_IDROPONICA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/9_cella_idroponica.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/9_cella_idroponica.sql.bak", lines)