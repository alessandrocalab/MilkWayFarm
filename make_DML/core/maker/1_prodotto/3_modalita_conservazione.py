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


#MODALITA_CONSERVAZIONE:NOME_CONSERVAZIONE DURATA_MASSIMA_GIORNI TEMPERATURA_MAX TEMPERATURA_MIN UMIDITA_MIN UMIDITA_MAX 

NOME_CONSERVAZIONE = []

DURATA_MASSIMA_GIORNI = []

TEMPERATURA_MAX = []

TEMPERATURA_MIN = []

UMIDITA_MIN = []

UMIDITA_MAX = []


theList=list(zip(NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX))

keys = ["NOME_CONSERVAZIONE", "DURATA_MASSIMA_GIORNI", "TEMPERATURA_MAX", "TEMPERATURA_MIN", "UMIDITA_MIN", "UMIDITA_MAX"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX\n"
for i in range(len(theList)):
  lines+=make_DML_line("MODALITA_CONSERVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/3_modalita_conservazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/3_modalita_conservazione.sql", lines)