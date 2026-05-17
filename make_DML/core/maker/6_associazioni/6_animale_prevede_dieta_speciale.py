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


#ANIMALE_PREVEDE_DIETA_SPECIALE:ETICHETTA_ANIMALE NOME_DIETA DATA_INIZIO DATA_FINE 

ETICHETTA_ANIMALE = []

NOME_DIETA = []

DATA_INIZIO = []

DATA_FINE = []



theDict=zip(ETICHETTA_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE)
theList=list(theDict)

lines="--ETICHETTA_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE"
for i in range(len(theList)):
   lines+=make_DML_line("ANIMALE_PREVEDE_DIETA_SPECIALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/6_animale_prevede_dieta_speciale.sql", lines)