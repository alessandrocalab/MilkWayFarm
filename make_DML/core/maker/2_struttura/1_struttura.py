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



theDict=zip(NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE)
theList=list(theDict)

lines="--NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE"
for i in range(len(theList)):
   lines+=make_DML_line("STRUTTURA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/1_struttura.sql", lines)