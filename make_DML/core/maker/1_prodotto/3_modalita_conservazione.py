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



theDict=zip(NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX)
theList=list(theDict)

lines="--NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX"
for i in range(len(theList)):
   lines+=make_DML_line("MODALITA_CONSERVAZIONE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML1_prodotto/3_modalita_conservazione.sql", lines)