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

ETICHETTA = [
    "'10000001'",
    "'10000002'",
    "'10000003'",
    "'10000004'",
    "'10000005'",
    "'10000006'",
    "'10000007'",
    "'10000008'",
    "'10000009'",
    "'10000010'",
    "'10000011'",
    "'10000012'",
    "'10000013'",
    "'10000014'",
    "'10000015'",
    "'10000016'",
    "'10000017'",
    "'10000018'",
    "'10000019'",
    "'10000020'",
    "'10000021'",
    "'10000022'",
    "'10000023'",
    "'10000024'",
    "'10000025'",
    "'10000026'",
    "'10000027'",
    "'10000028'",
    "'10000029'",
    "'10000030'"
]

DATA_USCITA = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "DATE '2025-11-20'",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "DATE '2025-09-12'",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "DATE '2025-12-05'",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

ETICHETTA_GENITORE = [
    "NULL",          # bovino fondatore
    "NULL",          # bovino fondatore
    "'10000002'",    # figlio di bovino
    "NULL",          # capra fondatrice
    "NULL",          # capra fondatrice
    "'10000005'",    # figlio di capra
    "NULL",          # pecora fondatrice
    "NULL",          # pecora fondatrice
    "'10000007'",    # figlio di pecora
    "NULL",          # coniglio fondatore
    "NULL",          # coniglio fondatore
    "'10000011'",    # figlio di coniglio
    "NULL",          # gallina fondatrice
    "NULL",          # gallo fondatore
    "'10000013'",    # pulcino
    "NULL",          # quaglia fondatrice
    "NULL",          # quaglia fondatrice
    "'10000017'",    # giovane quaglia
    "NULL",          # anatra fondatrice
    "NULL",          # anatra fondatrice
    "'10000020'",    # giovane anatra
    "NULL",          # maiale fondatore
    "NULL",          # maiale fondatore
    "'10000023'",    # giovane maiale
    "NULL",          # trota lotto base
    "NULL",          # trota lotto base
    "NULL",          # tilapia lotto base
    "NULL",          # tilapia lotto base
    "NULL",          # tacchino fondatore
    "NULL"           # oca fondatrice
]

SESSO = [
    "'M'",
    "'F'",
    "'F'",
    "'M'",
    "'F'",
    "'M'",
    "'F'",
    "'M'",
    "'F'",
    "'M'",
    "'F'",
    "'I'",
    "'F'",
    "'M'",
    "'I'",
    "'M'",
    "'F'",
    "'I'",
    "'M'",
    "'F'",
    "'I'",
    "'M'",
    "'F'",
    "'F'",
    "'I'",
    "'I'",
    "'I'",
    "'I'",
    "'M'",
    "'F'"
]

MESE_NASCITA = [
    3,
    5,
    9,
    2,
    6,
    11,
    4,
    7,
    1,
    8,
    10,
    2,
    3,
    3,
    6,
    5,
    5,
    9,
    4,
    4,
    8,
    1,
    2,
    6,
    7,
    7,
    9,
    9,
    11,
    12
]

ANNO_NASCITA = [
    2018,
    2019,
    2023,
    2019,
    2020,
    2024,
    2018,
    2019,
    2024,
    2020,
    2021,
    2025,
    2021,
    2021,
    2025,
    2022,
    2022,
    2025,
    2020,
    2021,
    2025,
    2019,
    2020,
    2024,
    2024,
    2024,
    2025,
    2025,
    2022,
    2021
]

DATA_INGRESSO = [
    "DATE '2018-10-20'",
    "DATE '2019-06-10'",
    "DATE '2023-10-05'",
    "DATE '2019-03-12'",
    "DATE '2020-07-15'",
    "DATE '2024-12-02'",
    "DATE '2018-11-05'",
    "DATE '2019-08-14'",
    "DATE '2024-02-10'",
    "DATE '2020-09-01'",
    "DATE '2021-11-05'",
    "DATE '2025-03-20'",
    "DATE '2021-04-01'",
    "DATE '2021-04-01'",
    "DATE '2025-06-25'",
    "DATE '2022-06-02'",
    "DATE '2022-06-02'",
    "DATE '2025-10-10'",
    "DATE '2020-05-20'",
    "DATE '2021-05-15'",
    "DATE '2025-09-01'",
    "DATE '2019-02-10'",
    "DATE '2020-03-05'",
    "DATE '2024-07-12'",
    "DATE '2024-08-01'",
    "DATE '2024-08-01'",
    "DATE '2025-10-01'",
    "DATE '2025-10-01'",
    "DATE '2022-12-15'",
    "DATE '2022-01-20'"
]

NOME_TIPO_ANIMALE = [
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",
    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",
    "'Trota iridea'",
    "'Trota iridea'",
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",
    "'Tacchino nano'",
    "'Oca domestica'"
]


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