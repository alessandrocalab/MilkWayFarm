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


#ANIMALE:ETICHETTA DATA_USCITA ETICHETTA_GENITORE SESSO MESE_NASCITA ANNO_NASCITA DATA_INGRESSO NOME_TIPO_ANIMALE 

ETICHETTA = []

DATA_USCITA = []

ETICHETTA_GENITORE = []

SESSO = []

MESE_NASCITA = []

ANNO_NASCITA = []

DATA_INGRESSO = []

NOME_TIPO_ANIMALE = []



theDict=zip(ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE)
theList=list(theDict)

lines="--ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE"
for i in range(len(theList)):
   lines+=make_DML_line("ANIMALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/2_animale.sql", lines)