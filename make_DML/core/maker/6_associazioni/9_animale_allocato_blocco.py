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


#ANIMALE_ALLOCATO_BLOCCO:NUMERO_BLOCCO NOME_STRUTTURA CODICE_AREA ETICHETTA_ANIMALE DATA_ALLOCAZIONE DATA_DEALLOCAIONE 

NUMERO_BLOCCO = []

NOME_STRUTTURA = []

CODICE_AREA = []

ETICHETTA_ANIMALE = []

DATA_ALLOCAZIONE = []

DATA_DEALLOCAIONE = []



theDict=zip(NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE)
theList=list(theDict)

lines="--NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE"
for i in range(len(theList)):
   lines+=make_DML_line("ANIMALE_ALLOCATO_BLOCCO", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/9_animale_allocato_blocco.sql", lines)