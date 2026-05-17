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


#STADIO_CRESCITA_INTOLLERANTE_SOSTANZA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE NOME_SOSTANZA 

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []

NOME_SOSTANZA = []



theDict=zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA)
theList=list(theDict)

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA"
for i in range(len(theList)):
   lines+=make_DML_line("STADIO_CRESCITA_INTOLLERANTE_SOSTANZA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/4_stadio_crescita_intollerante_sostanza.sql", lines)