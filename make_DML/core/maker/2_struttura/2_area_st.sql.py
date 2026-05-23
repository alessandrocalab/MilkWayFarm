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


#AREA_ST:CODICE_AREA NOME_STRUTTURA DATA_TERMINAZIONE TEMPERATURA_MIN TEMPERATURA_MAX UMIDITA_MIN UMIDITA_MAX LIVELLO_SICUREZZA PRESSIONE_PA VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

CODICE_AREA = []

NOME_STRUTTURA = []

DATA_TERMINAZIONE = []

TEMPERATURA_MIN = []

TEMPERATURA_MAX = []

UMIDITA_MIN = []

UMIDITA_MAX = []

LIVELLO_SICUREZZA = []

PRESSIONE_PA = []

VOLUME_M3 = []

SUPERFICIE_MQ = []

DATA_ATTIVAZIONE = []


theList=list(zip(CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["CODICE_AREA", "NOME_STRUTTURA", "DATA_TERMINAZIONE", "TEMPERATURA_MIN", "TEMPERATURA_MAX", "UMIDITA_MIN", "UMIDITA_MAX", "LIVELLO_SICUREZZA", "PRESSIONE_PA", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("AREA_ST", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/2_area_st.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/2_area_st.sql.bak", lines)