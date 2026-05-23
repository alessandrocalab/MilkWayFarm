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


theList=list(zip(NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE))

keys = ["NOME_SOSTANZA", "IS_POTENZIALE_ALLERGENE", "IS_POTENZIALE_INTOLLERANTE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE\n"
for i in range(len(theList)):
  lines+=make_DML_line("SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/2_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/2_sostanza.sql", lines)