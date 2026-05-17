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



theDict=zip(NOME_DIETA, OBIETTIVO_DIETA)
theList=list(theDict)

lines="--NOME_DIETA, OBIETTIVO_DIETA"
for i in range(len(theList)):
   lines+=make_DML_line("DIETA_ANIMALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/4_nome_animale.sql", lines)