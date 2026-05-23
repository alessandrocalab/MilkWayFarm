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


theList=list(zip(NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE))

keys = ["NUMERO_BLOCCO", "NOME_STRUTTURA", "CODICE_AREA", "ETICHETTA_ANIMALE", "DATA_ALLOCAZIONE", "DATA_DEALLOCAIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE_ALLOCATO_BLOCCO", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/9_animale_allocato_blocco.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/9_animale_allocato_blocco.sql", lines)