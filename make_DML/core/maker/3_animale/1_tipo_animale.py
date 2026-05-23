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


#TIPO_ANIMALE:NOME_TIPO_ANIMALE SPECIE VITA_MEDIA_ANNI MODALITA_RIPRODUZIONE GIORNI_GESTAZIONE UMIDITA_IDEALE SPAZIO_MINIMO_MQ TEMPERATURA_IDEALE 

NOME_TIPO_ANIMALE = []

SPECIE = []

VITA_MEDIA_ANNI = []

MODALITA_RIPRODUZIONE = []

GIORNI_GESTAZIONE = []

UMIDITA_IDEALE = []

SPAZIO_MINIMO_MQ = []

TEMPERATURA_IDEALE = []


theList=list(zip(NOME_TIPO_ANIMALE, SPECIE, VITA_MEDIA_ANNI, MODALITA_RIPRODUZIONE, GIORNI_GESTAZIONE, UMIDITA_IDEALE, SPAZIO_MINIMO_MQ, TEMPERATURA_IDEALE))

keys = ["NOME_TIPO_ANIMALE", "SPECIE", "VITA_MEDIA_ANNI", "MODALITA_RIPRODUZIONE", "GIORNI_GESTAZIONE", "UMIDITA_IDEALE", "SPAZIO_MINIMO_MQ", "TEMPERATURA_IDEALE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_TIPO_ANIMALE, SPECIE, VITA_MEDIA_ANNI, MODALITA_RIPRODUZIONE, GIORNI_GESTAZIONE, UMIDITA_IDEALE, SPAZIO_MINIMO_MQ, TEMPERATURA_IDEALE\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/1_tipo_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/1_tipo_animale.sql", lines)