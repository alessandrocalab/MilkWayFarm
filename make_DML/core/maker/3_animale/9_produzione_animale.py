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


#PRODUZIONE_ANIMALE:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA CODICE_AREA NOME_PRODOTTO QUANTITA 

DATA_PRODUZIONE = []

NUMERO_BLOCCO = []

NOME_STRUTTURA = []

CODICE_AREA = []

NOME_PRODOTTO = []

QUANTITA = []



theDict=zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, NOME_PRODOTTO, QUANTITA)
theList=list(theDict)

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, NOME_PRODOTTO, QUANTITA"
for i in range(len(theList)):
   lines+=make_DML_line("PRODUZIONE_ANIMALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/9_produzione_animale.sql", lines)