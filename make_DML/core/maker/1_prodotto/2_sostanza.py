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


#SOSTANZA:NOME_SOSTANZA IS_POTENZIALE_ALLERGENE IS_POTENZIALE_INTOLLERANTE 

NOME_SOSTANZA = []

IS_POTENZIALE_ALLERGENE = []

IS_POTENZIALE_INTOLLERANTE = []



theDict=zip(NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE)
theList=list(theDict)

lines="--NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE"
for i in range(len(theList)):
   lines+=make_DML_line("SOSTANZA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML1_prodotto/2_sostanza.sql", lines)