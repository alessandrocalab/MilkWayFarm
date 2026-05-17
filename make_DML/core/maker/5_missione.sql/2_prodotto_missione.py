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


#PRODOTTO_MISSIONE:NOME_PRODOTTO NOME_MISSIONE QUANTITA DATA_PRODUZIONE 

NOME_PRODOTTO = []

NOME_MISSIONE = []

QUANTITA = []

DATA_PRODUZIONE = []



theDict=zip(NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE)
theList=list(theDict)

lines="--NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE"
for i in range(len(theList)):
   lines+=make_DML_line("PRODOTTO_MISSIONE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML5_missione.sql/2_prodotto_missione.sql", lines)