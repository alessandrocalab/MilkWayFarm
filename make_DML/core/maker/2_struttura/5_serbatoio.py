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


#SERBATOIO:NUMERO_SERBATOIO CODICE_AREA NOME_STRUTTURA DATA_SMONTAGGIO DATA_MONTAGGIO PRESSIONE_MAX_PA DIMENSIONE_M3 

NUMERO_SERBATOIO = []

CODICE_AREA = []

NOME_STRUTTURA = []

DATA_SMONTAGGIO = []

DATA_MONTAGGIO = []

PRESSIONE_MAX_PA = []

DIMENSIONE_M3 = []


theList=list(zip(NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3))

keys = ["NUMERO_SERBATOIO", "CODICE_AREA", "NOME_STRUTTURA", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "PRESSIONE_MAX_PA", "DIMENSIONE_M3"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3\n"
for i in range(len(theList)):
  lines+=make_DML_line("SERBATOIO", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/5_serbatoio.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/5_serbatoio.sql", lines)