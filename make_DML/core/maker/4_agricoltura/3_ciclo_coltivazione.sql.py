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


#CICLO_COLTIVAZIONE:DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA DATA_FINE_EFFETTIVA QUANTITA_SEMI NOME_MOD_COLTIVAZIONE NOME_TIPO_COLTURA 

DATA_INIZIO = []

CODICE_CELLA_IDR = []

CODICE_AREA = []

NOME_STRUTTURA = []

DATA_FINE_EFFETTIVA = []

QUANTITA_SEMI = []

NOME_MOD_COLTIVAZIONE = []

NOME_TIPO_COLTURA = []


theList=list(zip(DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, QUANTITA_SEMI, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA))

keys = ["DATA_INIZIO", "CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "DATA_FINE_EFFETTIVA", "QUANTITA_SEMI", "NOME_MOD_COLTIVAZIONE", "NOME_TIPO_COLTURA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, QUANTITA_SEMI, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA\n"
for i in range(len(theList)):
  lines+=make_DML_line("CICLO_COLTIVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/3_ciclo_coltivazione.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/3_ciclo_coltivazione.sql.bak", lines)