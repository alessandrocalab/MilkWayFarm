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


#PRODUZIONE_ANIMALE_ALLOC_SCAFF:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA_BLOCCO CODICE_AREA_BLOCCO NOME_PRODOTTO NUMERO_SCAFFALE CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF QUANTITA_ALLOCATA 

DATA_PRODUZIONE = []

NUMERO_BLOCCO = []

NOME_STRUTTURA_BLOCCO = []

CODICE_AREA_BLOCCO = []

NOME_PRODOTTO = []

NUMERO_SCAFFALE = []

CODICE_AREA_SCAFF = []

NOME_STRUTTURA_SCAFF = []

QUANTITA_ALLOCATA = []



theDict=zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA)
theList=list(theDict)

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA"
for i in range(len(theList)):
   lines+=make_DML_line("PRODUZIONE_ANIMALE_ALLOC_SCAFF", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/18_produzione_animale_alloc_scaff.sql", lines)