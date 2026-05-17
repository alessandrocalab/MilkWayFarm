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


#TIPO_COLTURA_TIPO_PRODOTTO:NOME_TIPO_COLTURA NOME_PRODOTTO 

NOME_TIPO_COLTURA = []

NOME_PRODOTTO = []



theDict=zip(NOME_TIPO_COLTURA, NOME_PRODOTTO)
theList=list(theDict)

lines="--NOME_TIPO_COLTURA, NOME_PRODOTTO"
for i in range(len(theList)):
   lines+=make_DML_line("TIPO_COLTURA_TIPO_PRODOTTO", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/12_tipo_coltura_tipo_prodotto.SQL", lines)