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


#TIPO_SENSORE:NOME_PRODUTTORE NOME_MODELLO VALORE_MIN VALORE_MAX PRECISIONE GRANDEZZA_MISURATA UNITA_MISURA FREQUENZA_RILEVAMENTO_HZ 

NOME_PRODUTTORE = []

NOME_MODELLO = []

VALORE_MIN = []

VALORE_MAX = []

PRECISIONE = []

GRANDEZZA_MISURATA = []

UNITA_MISURA = []

FREQUENZA_RILEVAMENTO_HZ = []



theDict=zip(NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ)
theList=list(theDict)

lines="--NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ"
for i in range(len(theList)):
   lines+=make_DML_line("TIPO_SENSORE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML2_struttura/6_tipo_sensore.sql", lines)