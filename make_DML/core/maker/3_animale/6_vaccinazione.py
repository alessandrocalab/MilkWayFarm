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


#VACCINAZIONE:ETICHETTA_ANIMALE NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA DATA_VACCINAZIONE MATRICOLA_SOMMINISTRATORE 

ETICHETTA_ANIMALE = []

NOME_VACCINO = []

NOME_TIPO_ANIMALE = []

NOME_STADIO_CRESCITA = []

DATA_VACCINAZIONE = []

MATRICOLA_SOMMINISTRATORE = []



theDict=zip(ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE)
theList=list(theDict)

lines="--ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE"
for i in range(len(theList)):
   lines+=make_DML_line("VACCINAZIONE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/6_vaccinazione.sql", lines)