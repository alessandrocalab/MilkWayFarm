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


#PRODOTTO_MISSIONE_ALLOC_SERB:NOME_PRODOTTO NOME_MISSIONE NUMERO_SERBATOIO CODICE_AREA_SERB NOME_STRUTTURA_SERB QUANTITA_ALLOCATA 

NOME_PRODOTTO = []

NOME_MISSIONE = []

NUMERO_SERBATOIO = []

CODICE_AREA_SERB = []

NOME_STRUTTURA_SERB = []

QUANTITA_ALLOCATA = []



theDict=zip(NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA)
theList=list(theDict)

lines="--NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA"
for i in range(len(theList)):
   lines+=make_DML_line("PRODOTTO_MISSIONE_ALLOC_SERB", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/19_prodotto_missione_alloc_serb.sql", lines)