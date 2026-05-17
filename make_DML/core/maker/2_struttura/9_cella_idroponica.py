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



theDict=zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE)
theList=list(theDict)

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE"
for i in range(len(theList)):
   lines+=make_DML_line("CELLA_IDROPONICA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/9_cella_idroponica.sql", lines)