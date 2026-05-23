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


#STRUTTURA:NOME_STRUTTURA DATA_TERMINAZIONE QUOTA LONGITUDINE LATITUDINE VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

NOME_STRUTTURA = []

DATA_TERMINAZIONE = []

QUOTA = []

LONGITUDINE = []

LATITUDINE = []

VOLUME_M3 = []

SUPERFICIE_MQ = []

DATA_ATTIVAZIONE = []


theList=list(zip(NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["NOME_STRUTTURA", "DATA_TERMINAZIONE", "QUOTA", "LONGITUDINE", "LATITUDINE", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("STRUTTURA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/1_struttura.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/1_struttura.sql", lines)