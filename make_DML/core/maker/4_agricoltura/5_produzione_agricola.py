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


#PRODUZIONE_AGRICOLA:DATA_PRODUZIONE_AGRICOLA DATA_INIZIO_CICLO_COLTIVAZIONE CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA NOME_PRODOTTO QUANTITA 

DATA_PRODUZIONE_AGRICOLA = []

DATA_INIZIO_CICLO_COLTIVAZIONE = []

CODICE_CELLA_IDR = []

CODICE_AREA = []

NOME_STRUTTURA = []

NOME_PRODOTTO = []

QUANTITA = []



theDict=zip(DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA)
theList=list(theDict)

lines="--DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA"
for i in range(len(theList)):
   lines+=make_DML_line("PRODUZIONE_AGRICOLA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML4_agricoltura/5_produzione_agricola.sql", lines)