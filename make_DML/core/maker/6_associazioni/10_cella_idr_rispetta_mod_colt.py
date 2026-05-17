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


#CELLA_IDR_RISPETTA_MOD_COLT:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA NOME_MOD_COLTIVAZIONE 

CODICE_CELLA_IDR = []

CODICE_AREA = []

NOME_STRUTTURA = []

NOME_MOD_COLTIVAZIONE = []



theDict=zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE)
theList=list(theDict)

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE"
for i in range(len(theList)):
   lines+=make_DML_line("CELLA_IDR_RISPETTA_MOD_COLT", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/10_cella_idr_rispetta_mod_colt.sql", lines)