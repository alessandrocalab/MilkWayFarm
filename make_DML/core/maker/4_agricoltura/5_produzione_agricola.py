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


theList=list(zip(DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA))

keys = ["DATA_PRODUZIONE_AGRICOLA", "DATA_INIZIO_CICLO_COLTIVAZIONE", "CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "NOME_PRODOTTO", "QUANTITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_AGRICOLA", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/5_produzione_agricola.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/5_produzione_agricola.sql", lines)