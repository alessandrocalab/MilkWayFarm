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


#DIETA_COMPRENDE_PRODOTTO:NOME_PRODOTTO NOME_DIETA QUANTITA_GRAMMI 

NOME_PRODOTTO = []

NOME_DIETA = []

QUANTITA_GRAMMI = []



theDict=zip(NOME_PRODOTTO, NOME_DIETA, QUANTITA_GRAMMI)
theList=list(theDict)

lines="--NOME_PRODOTTO, NOME_DIETA, QUANTITA_GRAMMI"
for i in range(len(theList)):
   lines+=make_DML_line("DIETA_COMPRENDE_PRODOTTO", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/2_dieta_comprende_prodotto.sql", lines)