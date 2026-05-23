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


#VISITA_VETERINARIA:ETICHETTA_ANIMALE DATA_VISITA STATO_SALUTE TIPO_VISITA 

ETICHETTA_ANIMALE = []

DATA_VISITA = []

STATO_SALUTE = []

TIPO_VISITA = []


theList=list(zip(ETICHETTA_ANIMALE, DATA_VISITA, STATO_SALUTE, TIPO_VISITA))

keys = ["ETICHETTA_ANIMALE", "DATA_VISITA", "STATO_SALUTE", "TIPO_VISITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, DATA_VISITA, STATO_SALUTE, TIPO_VISITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("VISITA_VETERINARIA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/7_visita_veterinaria.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/7_visita_veterinaria.sql", lines)