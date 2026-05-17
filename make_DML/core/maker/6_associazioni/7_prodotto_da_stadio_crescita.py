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


#PRODOTTO_DA_STADIO_CRESCITA:NOME_PRODOTTO NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE 

NOME_PRODOTTO = []

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []



theDict=zip(NOME_PRODOTTO, NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE)
theList=list(theDict)

lines="--NOME_PRODOTTO, NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE"
for i in range(len(theList)):
   lines+=make_DML_line("PRODOTTO_DA_STADIO_CRESCITA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/7_prodotto_da_stadio_crescita.sql", lines)