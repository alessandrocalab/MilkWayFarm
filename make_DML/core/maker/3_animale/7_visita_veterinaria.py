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


#VISITA_VETERINARIA:ETICHETTA_ANIMALE DATA_VISITA MATRICOLA_VETERINARIO STATO_SALUTE TIPO_VISITA 

ETICHETTA_ANIMALE = []

DATA_VISITA = []

MATRICOLA_VETERINARIO = []

STATO_SALUTE = []

TIPO_VISITA = []



theDict=zip(ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA)
theList=list(theDict)

lines="--ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA"
for i in range(len(theList)):
   lines+=make_DML_line("VISITA_VETERINARIA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/7_visita_veterinaria.sql", lines)