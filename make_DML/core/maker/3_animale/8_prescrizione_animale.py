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



theDict=zip(NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA)
theList=list(theDict)

lines="--NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA"
for i in range(len(theList)):
   lines+=make_DML_line("PRESCRIZIONE_ANIMALE", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML3_animale/8_prescrizione_animale.sql", lines)