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



theDict=zip(SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE)
theList=list(theDict)

lines="--SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE"
for i in range(len(theList)):
   lines+=make_DML_line("REGISTRAZIONE_SENSORE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/8_registrazione_sensore.sql", lines)