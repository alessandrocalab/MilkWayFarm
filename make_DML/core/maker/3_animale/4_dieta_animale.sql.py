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


#DIETA_ANIMALE:NOME_DIETA OBIETTIVO_DIETA 

NOME_DIETA = []

OBIETTIVO_DIETA = []


theList=list(zip(NOME_DIETA, OBIETTIVO_DIETA))

keys = ["NOME_DIETA", "OBIETTIVO_DIETA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_DIETA, OBIETTIVO_DIETA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DIETA_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/4_dieta_animale.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/4_dieta_animale.sql.bak", lines)