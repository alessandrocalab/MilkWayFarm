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


#STADIO_CRESCITA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE LIVELLO_BIOSICUREZZA_MINIMO ETA_MINIMA_MESI 

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []

LIVELLO_BIOSICUREZZA_MINIMO = []

ETA_MINIMA_MESI = []


theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "LIVELLO_BIOSICUREZZA_MINIMO", "ETA_MINIMA_MESI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/3_stadio_crescita.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/3_stadio_crescita.sql.bak", lines)