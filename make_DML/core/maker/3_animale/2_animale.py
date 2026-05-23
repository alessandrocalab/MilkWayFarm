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


theList=list(zip(ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE))

keys = ["ETICHETTA", "DATA_USCITA", "ETICHETTA_GENITORE", "SESSO", "MESE_NASCITA", "ANNO_NASCITA", "DATA_INGRESSO", "NOME_TIPO_ANIMALE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/2_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/2_animale.sql", lines)