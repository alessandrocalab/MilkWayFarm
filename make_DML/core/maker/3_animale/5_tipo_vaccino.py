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

NOME_VACCINO = [
    # Bovino nano
    "'BOV-BASE-RESP'",
    "'BOV-RICHIAMO-RESP'",
    "'BOV-ENTERICO'",

    # Capra nana
    "'CAP-BASE-RESP'",
    "'CAP-RICHIAMO-RESP'",
    "'CAP-CLOSTRIDI'",

    # Pecora compatta
    "'PEC-BASE-RESP'",
    "'PEC-RICHIAMO-RESP'",
    "'PEC-CLOSTRIDI'",

    # Coniglio europeo
    "'CON-MIXO'",
    "'CON-RICHIAMO-MIXO'",
    "'CON-ENTERITE'",

    # Gallina ovaiola
    "'GAL-MAREK'",
    "'GAL-NEWCASTLE'",
    "'GAL-RICHIAMO-NEWCASTLE'",

    # Quaglia giapponese
    "'QUA-NEWCASTLE'",
    "'QUA-RICHIAMO-NEWCASTLE'",

    # Anatra domestica
    "'ANA-PASTEURELLOSI'",
    "'ANA-RICHIAMO-PASTEURELLOSI'",

    # Maiale nano
    "'MAI-BASE-RESP'",
    "'MAI-RICHIAMO-RESP'",
    "'MAI-ENTERICO'",

    # Trota iridea
    "'TRO-SETTICEMIA'",
    "'TRO-RICHIAMO-SETTICEMIA'",

    # Tilapia nilotica
    "'TIL-STREPTOCOCCOSI'",
    "'TIL-RICHIAMO-STREPTOCOCCOSI'",

    # Tacchino nano
    "'TAC-NEWCASTLE'",
    "'TAC-RICHIAMO-NEWCASTLE'",

    # Oca domestica
    "'OCA-PASTEURELLOSI'",
    "'OCA-RICHIAMO-PASTEURELLOSI'"
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

    # Anatra domestica
    "'Anatra domestica'",
    "'Anatra domestica'",

    # Maiale nano
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",

    # Trota iridea
    "'Trota iridea'",
    "'Trota iridea'",

    # Tilapia nilotica
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",

    # Tacchino nano
    "'Tacchino nano'",
    "'Tacchino nano'",

    # Oca domestica
    "'Oca domestica'",
    "'Oca domestica'"
]

NOME_STADIO_CRESCITA = [
    # Bovino nano
    "'Vitello'",
    "'Giovane'",
    "'Vitello'",

    # Capra nana
    "'Capretto'",
    "'Giovane'",
    "'Capretto'",

    # Pecora compatta
    "'Agnello'",
    "'Giovane'",
    "'Agnello'",

    # Coniglio europeo
    "'Cucciolo'",
    "'Giovane'",
    "'Cucciolo'",

    # Gallina ovaiola
    "'Pulcino'",
    "'Pollastra'",
    "'Adulto'",

    # Quaglia giapponese
    "'Pulcino'",
    "'Giovane'",

    # Anatra domestica
    "'Anatroccolo'",
    "'Giovane'",

    # Maiale nano
    "'Suinetto'",
    "'Giovane'",
    "'Suinetto'",

    # Trota iridea
    "'Avannotto'",
    "'Giovane'",

    # Tilapia nilotica
    "'Avannotto'",
    "'Giovane'",

    # Tacchino nano
    "'Pulcino'",
    "'Giovane'",

    # Oca domestica
    "'Papero'",
    "'Giovane'"
]

NOME_VACCINO_PROPEDEUTICO = [
    # Bovino nano
    "NULL",
    "'BOV-BASE-RESP'",
    "NULL",

    # Capra nana
    "NULL",
    "'CAP-BASE-RESP'",
    "NULL",

    # Pecora compatta
    "NULL",
    "'PEC-BASE-RESP'",
    "NULL",

    # Coniglio europeo
    "NULL",
    "'CON-MIXO'",
    "NULL",

    # Gallina ovaiola
    "NULL",
    "NULL",
    "'GAL-NEWCASTLE'",

    # Quaglia giapponese
    "NULL",
    "'QUA-NEWCASTLE'",

    # Anatra domestica
    "NULL",
    "'ANA-PASTEURELLOSI'",

    # Maiale nano
    "NULL",
    "'MAI-BASE-RESP'",
    "NULL",

    # Trota iridea
    "NULL",
    "'TRO-SETTICEMIA'",

    # Tilapia nilotica
    "NULL",
    "'TIL-STREPTOCOCCOSI'",

    # Tacchino nano
    "NULL",
    "'TAC-NEWCASTLE'",

    # Oca domestica
    "NULL",
    "'OCA-PASTEURELLOSI'"
]

NOME_STADIO_CRESCITA_PROPEDEUTICO = [
    # Bovino nano
    "NULL",
    "'Vitello'",
    "NULL",

    # Capra nana
    "NULL",
    "'Capretto'",
    "NULL",

    # Pecora compatta
    "NULL",
    "'Agnello'",
    "NULL",

    # Coniglio europeo
    "NULL",
    "'Cucciolo'",
    "NULL",

    # Gallina ovaiola
    "NULL",
    "NULL",
    "'Pollastra'",

    # Quaglia giapponese
    "NULL",
    "'Pulcino'",

    # Anatra domestica
    "NULL",
    "'Anatroccolo'",

    # Maiale nano
    "NULL",
    "'Suinetto'",
    "NULL",

    # Trota iridea
    "NULL",
    "'Avannotto'",

    # Tilapia nilotica
    "NULL",
    "'Avannotto'",

    # Tacchino nano
    "NULL",
    "'Pulcino'",

    # Oca domestica
    "NULL",
    "'Papero'"
]

NOME_TIPO_ANIMALE_PROPEDEUTICO = [
    # Bovino nano
    "NULL",
    "'Bovino nano'",
    "NULL",

    # Capra nana
    "NULL",
    "'Capra nana'",
    "NULL",

    # Pecora compatta
    "NULL",
    "'Pecora compatta'",
    "NULL",

    # Coniglio europeo
    "NULL",
    "'Coniglio europeo'",
    "NULL",

    # Gallina ovaiola
    "NULL",
    "NULL",
    "'Gallina ovaiola'",

    # Quaglia giapponese
    "NULL",
    "'Quaglia giapponese'",

    # Anatra domestica
    "NULL",
    "'Anatra domestica'",

    # Maiale nano
    "NULL",
    "'Maiale nano'",
    "NULL",

    # Trota iridea
    "NULL",
    "'Trota iridea'",

    # Tilapia nilotica
    "NULL",
    "'Tilapia nilotica'",

    # Tacchino nano
    "NULL",
    "'Tacchino nano'",

    # Oca domestica
    "NULL",
    "'Oca domestica'"
]

IS_VACCINO_OBBLIGATORIO = [
    # Bovino nano
    1,
    1,
    1,

    # Capra nana
    1,
    1,
    1,

    # Pecora compatta
    1,
    1,
    1,

    # Coniglio europeo
    1,
    1,
    0,

    # Gallina ovaiola
    1,
    1,
    1,

    # Quaglia giapponese
    1,
    1,

    # Anatra domestica
    1,
    1,

    # Maiale nano
    1,
    1,
    1,

    # Trota iridea
    1,
    1,

    # Tilapia nilotica
    1,
    1,

    # Tacchino nano
    1,
    1,

    # Oca domestica
    1,
    1
]

ETA_MINIMA_MESI = [
    # Bovino nano
    1,
    6,
    2,

    # Capra nana
    1,
    4,
    2,

    # Pecora compatta
    1,
    4,
    2,

    # Coniglio europeo
    1,
    2,
    1,

    # Gallina ovaiola
    0,
    2,
    5,

    # Quaglia giapponese
    0,
    1,

    # Anatra domestica
    1,
    2,

    # Maiale nano
    1,
    3,
    2,

    # Trota iridea
    0,
    3,

    # Tilapia nilotica
    0,
    2,

    # Tacchino nano
    0,
    2,

    # Oca domestica
    1,
    3
]

DOSE_ML = [
    # Bovino nano
    2.00,
    2.00,
    1.50,

    # Capra nana
    1.00,
    1.00,
    1.00,

    # Pecora compatta
    1.00,
    1.00,
    1.00,

    # Coniglio europeo
    0.50,
    0.50,
    0.30,

    # Gallina ovaiola
    0.20,
    0.30,
    0.30,

    # Quaglia giapponese
    0.10,
    0.10,

    # Anatra domestica
    0.30,
    0.30,

    # Maiale nano
    1.50,
    1.50,
    1.00,

    # Trota iridea
    0.05,
    0.05,

    # Tilapia nilotica
    0.05,
    0.05,

    # Tacchino nano
    0.30,
    0.30,

    # Oca domestica
    0.40,
    0.40
]

theList=list(zip(NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML))

keys = ["NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "NOME_VACCINO_PROPEDEUTICO", "NOME_STADIO_CRESCITA_PROPEDEUTICO", "NOME_TIPO_ANIMALE_PROPEDEUTICO", "IS_VACCINO_OBBLIGATORIO", "ETA_MINIMA_MESI", "DOSE_ML"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINO", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/5_tipo_vaccino.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/5_tipo_vaccino.sql", lines)