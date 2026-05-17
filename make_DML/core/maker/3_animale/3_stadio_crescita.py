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

NOME_STADIO_CRESCITA = [
    # Bovino nano
    "'Vitello'",
    "'Giovane'",
    "'Adulto'",

    # Capra nana
    "'Capretto'",
    "'Giovane'",
    "'Adulto'",

    # Pecora compatta
    "'Agnello'",
    "'Giovane'",
    "'Adulto'",

    # Coniglio europeo
    "'Cucciolo'",
    "'Giovane'",
    "'Adulto'",

    # Gallina ovaiola
    "'Pulcino'",
    "'Pollastra'",
    "'Adulto'",

    # Quaglia giapponese
    "'Pulcino'",
    "'Giovane'",
    "'Adulto'",

    # Anatra domestica
    "'Anatroccolo'",
    "'Giovane'",
    "'Adulto'",

    # Maiale nano
    "'Suinetto'",
    "'Giovane'",
    "'Adulto'",

    # Trota iridea
    "'Avannotto'",
    "'Giovane'",
    "'Adulto'",

    # Tilapia nilotica
    "'Avannotto'",
    "'Giovane'",
    "'Adulto'",

    # Tacchino nano
    "'Pulcino'",
    "'Giovane'",
    "'Adulto'",

    # Oca domestica
    "'Papero'",
    "'Giovane'",
    "'Adulto'"
]

NOME_TIPO_ANIMALE = [
    # Bovino nano
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",

    # Capra nana
    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",

    # Pecora compatta
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",

    # Coniglio europeo
    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",

    # Gallina ovaiola
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",

    # Quaglia giapponese
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",

    # Anatra domestica
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",

    # Maiale nano
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",

    # Trota iridea
    "'Trota iridea'",
    "'Trota iridea'",
    "'Trota iridea'",

    # Tilapia nilotica
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",

    # Tacchino nano
    "'Tacchino nano'",
    "'Tacchino nano'",
    "'Tacchino nano'",

    # Oca domestica
    "'Oca domestica'",
    "'Oca domestica'",
    "'Oca domestica'"
]

LIVELLO_BIOSICUREZZA_MINIMO = [
    # Bovino nano
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Capra nana
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Pecora compatta
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Coniglio europeo
    "'BASSO'",
    "'BASSO'",
    "'BASSO'",

    # Gallina ovaiola
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Quaglia giapponese
    "'BASSO'",
    "'BASSO'",
    "'BASSO'",

    # Anatra domestica
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Maiale nano
    "'ALTO'",
    "'ALTO'",
    "'ALTO'",

    # Trota iridea
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Tilapia nilotica
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Tacchino nano
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'",

    # Oca domestica
    "'MEDIO'",
    "'MEDIO'",
    "'MEDIO'"
]

ETA_MINIMA_MESI = [
    # Bovino nano
    0,
    6,
    24,

    # Capra nana
    0,
    4,
    12,

    # Pecora compatta
    0,
    4,
    12,

    # Coniglio europeo
    0,
    2,
    6,

    # Gallina ovaiola
    0,
    2,
    5,

    # Quaglia giapponese
    0,
    1,
    2,

    # Anatra domestica
    0,
    2,
    5,

    # Maiale nano
    0,
    3,
    8,

    # Trota iridea
    0,
    3,
    12,

    # Tilapia nilotica
    0,
    2,
    6,

    # Tacchino nano
    0,
    2,
    6,

    # Oca domestica
    0,
    3,
    9
]

theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "LIVELLO_BIOSICUREZZA_MINIMO", "ETA_MINIMA_MESI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/3_stadio_crescita.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/3_stadio_crescita.sql", lines)