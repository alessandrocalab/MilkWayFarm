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

NOME_TIPO_ANIMALE = [
    "'Bovino nano'",
    "'Capra nana'",
    "'Pecora compatta'",
    "'Coniglio europeo'",
    "'Gallina ovaiola'",
    "'Quaglia giapponese'",
    "'Anatra domestica'",
    "'Maiale nano'",
    "'Trota iridea'",
    "'Tilapia nilotica'",
    "'Tacchino nano'",
    "'Oca domestica'"
]

SPECIE = [
    "'Bos taurus'",
    "'Capra hircus'",
    "'Ovis aries'",
    "'Oryctolagus cuniculus'",
    "'Gallus gallus domesticus'",
    "'Coturnix japonica'",
    "'Anas platyrhynchos domesticus'",
    "'Sus scrofa domesticus'",
    "'Oncorhynchus mykiss'",
    "'Oreochromis niloticus'",
    "'Meleagris gallopavo'",
    "'Anser anser domesticus'"
]

VITA_MEDIA_ANNI = [
    18,
    12,
    11,
    8,
    7,
    3,
    8,
    12,
    6,
    8,
    6,
    15
]

MODALITA_RIPRODUZIONE = [
    "'VIVIPARA'",
    "'VIVIPARA'",
    "'VIVIPARA'",
    "'VIVIPARA'",
    "'OVIPARA'",
    "'OVIPARA'",
    "'OVIPARA'",
    "'VIVIPARA'",
    "'OVIPARA'",
    "'OVIPARA'",
    "'OVIPARA'",
    "'OVIPARA'"
]

GIORNI_GESTAZIONE = [
    283,
    150,
    147,
    31,
    "NULL",
    "NULL",
    "NULL",
    114,
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

UMIDITA_IDEALE = [
    60,
    55,
    55,
    60,
    60,
    55,
    65,
    60,
    95,
    95,
    60,
    65
]

SPAZIO_MINIMO_MQ = [
    8.00,
    2.00,
    2.00,
    0.80,
    0.25,
    0.08,
    0.50,
    3.00,
    0.15,
    0.12,
    0.40,
    0.70
]

TEMPERATURA_IDEALE = [
    291.15,  # 18°C
    290.15,  # 17°C
    289.15,  # 16°C
    293.15,  # 20°C
    294.15,  # 21°C
    295.15,  # 22°C
    293.15,  # 20°C
    294.15,  # 21°C
    285.15,  # 12°C
    300.15,  # 27°C
    293.15,  # 20°C
    292.15   # 19°C
]


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