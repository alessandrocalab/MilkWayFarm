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


#VACCINAZIONE:ETICHETTA_ANIMALE NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA DATA_VACCINAZIONE MATRICOLA_SOMMINISTRATORE 

ETICHETTA_ANIMALE = [
    "'10000001'",
    "'10000001'",
    "'10000002'",
    "'10000002'",
    "'10000003'",
    "'10000003'",

    "'10000004'",
    "'10000004'",
    "'10000005'",
    "'10000005'",
    "'10000006'",
    "'10000006'",

    "'10000007'",
    "'10000007'",
    "'10000008'",
    "'10000008'",
    "'10000009'",
    "'10000009'",

    "'10000010'",
    "'10000010'",
    "'10000011'",
    "'10000011'",
    "'10000012'",

    "'10000013'",
    "'10000013'",
    "'10000014'",
    "'10000014'",
    "'10000015'",
    "'10000015'",

    "'10000016'",
    "'10000016'",
    "'10000017'",
    "'10000017'",
    "'10000018'",
    "'10000018'",

    "'10000019'",
    "'10000019'",
    "'10000020'",
    "'10000020'",
    "'10000021'",
    "'10000021'",

    "'10000022'",
    "'10000022'",
    "'10000023'",
    "'10000023'",
    "'10000024'",
    "'10000024'",

    "'10000025'",
    "'10000025'",
    "'10000026'",
    "'10000026'",
    "'10000027'",
    "'10000027'",
    "'10000028'",
    "'10000028'",

    "'10000029'",
    "'10000029'",
    "'10000030'",
    "'10000030'"
]

NOME_VACCINO = [
    "'BOV-BASE-RESP'",
    "'BOV-RICHIAMO-RESP'",
    "'BOV-BASE-RESP'",
    "'BOV-RICHIAMO-RESP'",
    "'BOV-BASE-RESP'",
    "'BOV-ENTERICO'",

    "'CAP-BASE-RESP'",
    "'CAP-RICHIAMO-RESP'",
    "'CAP-BASE-RESP'",
    "'CAP-RICHIAMO-RESP'",
    "'CAP-BASE-RESP'",
    "'CAP-CLOSTRIDI'",

    "'PEC-BASE-RESP'",
    "'PEC-RICHIAMO-RESP'",
    "'PEC-BASE-RESP'",
    "'PEC-RICHIAMO-RESP'",
    "'PEC-BASE-RESP'",
    "'PEC-CLOSTRIDI'",

    "'CON-MIXO'",
    "'CON-RICHIAMO-MIXO'",
    "'CON-MIXO'",
    "'CON-RICHIAMO-MIXO'",
    "'CON-ENTERITE'",

    "'GAL-MAREK'",
    "'GAL-NEWCASTLE'",
    "'GAL-MAREK'",
    "'GAL-NEWCASTLE'",
    "'GAL-NEWCASTLE'",
    "'GAL-RICHIAMO-NEWCASTLE'",

    "'QUA-NEWCASTLE'",
    "'QUA-RICHIAMO-NEWCASTLE'",
    "'QUA-NEWCASTLE'",
    "'QUA-RICHIAMO-NEWCASTLE'",
    "'QUA-NEWCASTLE'",
    "'QUA-RICHIAMO-NEWCASTLE'",

    "'ANA-PASTEURELLOSI'",
    "'ANA-RICHIAMO-PASTEURELLOSI'",
    "'ANA-PASTEURELLOSI'",
    "'ANA-RICHIAMO-PASTEURELLOSI'",
    "'ANA-PASTEURELLOSI'",
    "'ANA-RICHIAMO-PASTEURELLOSI'",

    "'MAI-BASE-RESP'",
    "'MAI-RICHIAMO-RESP'",
    "'MAI-BASE-RESP'",
    "'MAI-RICHIAMO-RESP'",
    "'MAI-BASE-RESP'",
    "'MAI-ENTERICO'",

    "'TRO-SETTICEMIA'",
    "'TRO-RICHIAMO-SETTICEMIA'",
    "'TRO-SETTICEMIA'",
    "'TRO-RICHIAMO-SETTICEMIA'",
    "'TIL-STREPTOCOCCOSI'",
    "'TIL-RICHIAMO-STREPTOCOCCOSI'",
    "'TIL-STREPTOCOCCOSI'",
    "'TIL-RICHIAMO-STREPTOCOCCOSI'",

    "'TAC-NEWCASTLE'",
    "'TAC-RICHIAMO-NEWCASTLE'",
    "'OCA-PASTEURELLOSI'",
    "'OCA-RICHIAMO-PASTEURELLOSI'"
]

NOME_TIPO_ANIMALE = [
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",
    "'Bovino nano'",

    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",
    "'Capra nana'",

    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",
    "'Pecora compatta'",

    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",
    "'Coniglio europeo'",

    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",
    "'Gallina ovaiola'",

    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",
    "'Quaglia giapponese'",

    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",
    "'Anatra domestica'",

    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",
    "'Maiale nano'",

    "'Trota iridea'",
    "'Trota iridea'",
    "'Trota iridea'",
    "'Trota iridea'",
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",
    "'Tilapia nilotica'",

    "'Tacchino nano'",
    "'Tacchino nano'",
    "'Oca domestica'",
    "'Oca domestica'"
]

NOME_STADIO_CRESCITA = [
    "'Vitello'",
    "'Giovane'",
    "'Vitello'",
    "'Giovane'",
    "'Vitello'",
    "'Vitello'",

    "'Capretto'",
    "'Giovane'",
    "'Capretto'",
    "'Giovane'",
    "'Capretto'",
    "'Capretto'",

    "'Agnello'",
    "'Giovane'",
    "'Agnello'",
    "'Giovane'",
    "'Agnello'",
    "'Agnello'",

    "'Cucciolo'",
    "'Giovane'",
    "'Cucciolo'",
    "'Giovane'",
    "'Cucciolo'",

    "'Pulcino'",
    "'Pollastra'",
    "'Pulcino'",
    "'Pollastra'",
    "'Pollastra'",
    "'Adulto'",

    "'Pulcino'",
    "'Giovane'",
    "'Pulcino'",
    "'Giovane'",
    "'Pulcino'",
    "'Giovane'",

    "'Anatroccolo'",
    "'Giovane'",
    "'Anatroccolo'",
    "'Giovane'",
    "'Anatroccolo'",
    "'Giovane'",

    "'Suinetto'",
    "'Giovane'",
    "'Suinetto'",
    "'Giovane'",
    "'Suinetto'",
    "'Suinetto'",

    "'Avannotto'",
    "'Giovane'",
    "'Avannotto'",
    "'Giovane'",
    "'Avannotto'",
    "'Giovane'",
    "'Avannotto'",
    "'Giovane'",

    "'Pulcino'",
    "'Giovane'",
    "'Papero'",
    "'Giovane'"
]

DATA_VACCINAZIONE = [
    "DATE '2018-12-01'",
    "DATE '2019-05-20'",
    "DATE '2019-07-15'",
    "DATE '2020-01-20'",
    "DATE '2023-11-10'",
    "DATE '2023-12-05'",

    "DATE '2019-04-15'",
    "DATE '2019-08-20'",
    "DATE '2020-08-20'",
    "DATE '2021-01-10'",
    "DATE '2025-01-10'",
    "DATE '2025-02-05'",

    "DATE '2018-12-20'",
    "DATE '2019-05-15'",
    "DATE '2019-09-20'",
    "DATE '2020-02-10'",
    "DATE '2024-03-01'",
    "DATE '2024-03-28'",

    "DATE '2020-10-10'",
    "DATE '2020-12-15'",
    "DATE '2021-12-05'",
    "DATE '2022-01-25'",
    "DATE '2025-04-20'",

    "DATE '2021-04-05'",
    "DATE '2021-06-20'",
    "DATE '2021-04-05'",
    "DATE '2021-06-20'",
    "DATE '2025-08-01'",
    "DATE '2025-11-30'",

    "DATE '2022-06-10'",
    "DATE '2022-07-20'",
    "DATE '2022-06-10'",
    "DATE '2022-07-20'",
    "DATE '2025-10-20'",
    "DATE '2025-12-01'",

    "DATE '2020-06-15'",
    "DATE '2020-08-01'",
    "DATE '2021-06-10'",
    "DATE '2021-08-01'",
    "DATE '2025-09-15'",
    "DATE '2025-11-01'",

    "DATE '2019-03-20'",
    "DATE '2019-06-15'",
    "DATE '2020-04-10'",
    "DATE '2020-07-10'",
    "DATE '2024-09-15'",
    "DATE '2024-10-20'",

    "DATE '2024-08-15'",
    "DATE '2024-11-20'",
    "DATE '2024-08-15'",
    "DATE '2024-11-20'",
    "DATE '2025-10-15'",
    "DATE '2026-01-20'",
    "DATE '2025-10-15'",
    "DATE '2026-01-20'",

    "DATE '2023-01-20'",
    "DATE '2023-04-20'",
    "DATE '2022-02-25'",
    "DATE '2022-05-25'"
]

MATRICOLA_SOMMINISTRATORE = [
    "'VET001'",
    "'VET001'",
    "'VET002'",
    "'VET002'",
    "'VET001'",
    "'VET003'",

    "'VET002'",
    "'VET002'",
    "'VET001'",
    "'VET001'",
    "'VET003'",
    "'VET003'",

    "'VET001'",
    "'VET001'",
    "'VET002'",
    "'VET002'",
    "'VET003'",
    "'VET003'",

    "'VET004'",
    "'VET004'",
    "'VET004'",
    "'VET004'",
    "'VET003'",

    "'VET005'",
    "'VET005'",
    "'VET005'",
    "'VET005'",
    "'VET002'",
    "'VET002'",

    "'VET005'",
    "'VET005'",
    "'VET005'",
    "'VET005'",
    "'VET002'",
    "'VET002'",

    "'VET003'",
    "'VET003'",
    "'VET003'",
    "'VET003'",
    "'VET004'",
    "'VET004'",

    "'VET001'",
    "'VET001'",
    "'VET002'",
    "'VET002'",
    "'VET003'",
    "'VET003'",

    "'VET006'",
    "'VET006'",
    "'VET006'",
    "'VET006'",
    "'VET006'",
    "'VET006'",
    "'VET006'",
    "'VET006'",

    "'VET005'",
    "'VET005'",
    "'VET004'",
    "'VET004'"
]


theList=list(zip(ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE))

keys = ["ETICHETTA_ANIMALE", "NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "DATA_VACCINAZIONE", "MATRICOLA_SOMMINISTRATORE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/6_vaccinazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/6_vaccinazione.sql", lines)