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



theDict=zip(NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, DATA_SMONTAGGIO, SUPERFICIE_MQ, LIMITE_ALLOCAZIONE, DATA_MONTAGGIO)
theList=list(theDict)

lines="--NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, DATA_SMONTAGGIO, SUPERFICIE_MQ, LIMITE_ALLOCAZIONE, DATA_MONTAGGIO"
for i in range(len(theList)):
   lines+=make_DML_line("BLOCCO_ANIMALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/3_blocco_animale.sql", lines)