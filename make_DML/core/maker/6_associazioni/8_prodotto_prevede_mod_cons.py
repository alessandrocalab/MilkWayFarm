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


#PRODOTTO_PREVEDE_MOD_CONS:NOME_CONSERVAZIONE NOME_PRODOTTO 

NOME_CONSERVAZIONE = []

NOME_PRODOTTO = []



theDict=zip(NOME_CONSERVAZIONE, NOME_PRODOTTO)
theList=list(theDict)

lines="--NOME_CONSERVAZIONE, NOME_PRODOTTO"
for i in range(len(theList)):
   lines+=make_DML_line("PRODOTTO_PREVEDE_MOD_CONS", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/8_prodotto_prevede_mod_cons.sql", lines)