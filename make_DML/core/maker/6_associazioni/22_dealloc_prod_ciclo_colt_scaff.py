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


#DEALLOC_PROD_CICLO_COLT_SCAFF:DATE_MIN NOME_PRODOTTO NUMERO_SCAFF CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA QUANTITA_DEALLOCATA 

DATE_MIN = []

NOME_PRODOTTO = []

NUMERO_SCAFF = []

CODICE_AREA_SCAFF = []

NOME_STRUTTURA_SCAFF = []

DATA_INIZIO = []

CODICE_CELLA_IDR = []

CODICE_AREA_CELLA = []

NOME_STRUTTURA_CELLA = []

QUANTITA_DEALLOCATA = []



theDict=zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA)
theList=list(theDict)

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA"
for i in range(len(theList)):
   lines+=make_DML_line("DEALLOC_PROD_CICLO_COLT_SCAFF", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML6_associazioni/22_dealloc_prod_ciclo_colt_scaff.sql", lines)