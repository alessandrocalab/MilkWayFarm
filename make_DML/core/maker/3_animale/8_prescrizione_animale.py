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


#PRESCRIZIONE_ANIMALE:NOME_FARMACO ETICHETTA_ANIMALE DATA_VISITA NOME_PRODOTTO UNITA_MISURA DURATA_GIORNI QUANTITA_GIORNALIERA 

NOME_FARMACO = []

ETICHETTA_ANIMALE = []

DATA_VISITA = []

NOME_PRODOTTO = []

UNITA_MISURA = []

DURATA_GIORNI = []

QUANTITA_GIORNALIERA = []


theList=list(zip(NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA))

keys = ["NOME_FARMACO", "ETICHETTA_ANIMALE", "DATA_VISITA", "NOME_PRODOTTO", "UNITA_MISURA", "DURATA_GIORNI", "QUANTITA_GIORNALIERA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRESCRIZIONE_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/8_prescrizione_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/8_prescrizione_animale.sql", lines)