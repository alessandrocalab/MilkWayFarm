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


#STADIO_CRESCITA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE LIVELLO_BIOSICUREZZA_MINIMO ETA_MINIMA_MESI 

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []

LIVELLO_BIOSICUREZZA_MINIMO = []

ETA_MINIMA_MESI = []



theDict=zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI)
theList=list(theDict)

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI"
for i in range(len(theList)):
   lines+=make_DML_line("STADIO_CRESCITA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/3_stadio_crescita.sql", lines)