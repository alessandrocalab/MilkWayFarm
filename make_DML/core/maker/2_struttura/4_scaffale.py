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



theDict=zip(NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3)
theList=list(theDict)

lines="--NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3"
for i in range(len(theList)):
   lines+=make_DML_line("SCAFFALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/4_scaffale.sql", lines)