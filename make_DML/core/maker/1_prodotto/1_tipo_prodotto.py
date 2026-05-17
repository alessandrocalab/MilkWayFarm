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


#TIPO_PRODOTTO:NOME_PRODOTTO ALCOL FIBRE PROTEINE GRASSI CARBOIDRATI UNITA_MISURA IS_EDIBILE 

NOME_PRODOTTO = []

ALCOL = []

FIBRE = []

PROTEINE = []

GRASSI = []

CARBOIDRATI = []

UNITA_MISURA = []

IS_EDIBILE = []



theDict=zip(NOME_PRODOTTO, ALCOL, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE)
theList=list(theDict)

lines="--NOME_PRODOTTO, ALCOL, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE"
for i in range(len(theList)):
   lines+=make_DML_line("TIPO_PRODOTTO", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML1_prodotto/1_tipo_prodotto.sql", lines)