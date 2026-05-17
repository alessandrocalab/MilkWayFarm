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


theList=list(zip(ETICHETTA_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE))

keys = ["ETICHETTA_ANIMALE", "NOME_DIETA", "DATA_INIZIO", "DATA_FINE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE_PREVEDE_DIETA_SPECIALE", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/6_animale_prevede_dieta_speciale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/6_animale_prevede_dieta_speciale.sql", lines)