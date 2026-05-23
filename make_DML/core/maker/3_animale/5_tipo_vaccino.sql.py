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


#VACCINO:NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA NOME_VACCINO_PROPEDEUTICO NOME_STADIO_CRESCITA_PROPEDEUTICO NOME_TIPO_ANIMALE_PROPEDEUTICO IS_VACCINO_OBBLIGATORIO ETA_MINIMA_MESI DOSE_ML 

NOME_VACCINO = []

NOME_TIPO_ANIMALE = []

NOME_STADIO_CRESCITA = []

NOME_VACCINO_PROPEDEUTICO = []

NOME_STADIO_CRESCITA_PROPEDEUTICO = []

NOME_TIPO_ANIMALE_PROPEDEUTICO = []

IS_VACCINO_OBBLIGATORIO = []

ETA_MINIMA_MESI = []

DOSE_ML = []


theList=list(zip(NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML))

keys = ["NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "NOME_VACCINO_PROPEDEUTICO", "NOME_STADIO_CRESCITA_PROPEDEUTICO", "NOME_TIPO_ANIMALE_PROPEDEUTICO", "IS_VACCINO_OBBLIGATORIO", "ETA_MINIMA_MESI", "DOSE_ML"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINO", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/5_tipo_vaccino.sql.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/5_tipo_vaccino.sql.bak", lines)