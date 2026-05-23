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


#VACCINAZIONE:ETICHETTA_ANIMALE NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA DATA_VACCINAZIONE 

ETICHETTA_ANIMALE = []

NOME_VACCINO = []

NOME_TIPO_ANIMALE = []

NOME_STADIO_CRESCITA = []

DATA_VACCINAZIONE = []


theList=list(zip(ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE))

keys = ["ETICHETTA_ANIMALE", "NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "DATA_VACCINAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/6_vaccinazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/6_vaccinazione.sql", lines)