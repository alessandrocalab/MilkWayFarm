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


#VISITA_VETERINARIA:ETICHETTA_ANIMALE DATA_VISITA MATRICOLA_VETERINARIO STATO_SALUTE TIPO_VISITA 

ETICHETTA_ANIMALE = [
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
    "'10000030'",

    "'10000001'",
    "'10000005'",
    "'10000013'",
    "'10000022'",
    "'10000027'"
]

DATA_VISITA = [
    "DATE '2024-01-15'",
    "DATE '2024-01-18'",
    "DATE '2024-02-10'",
    "DATE '2024-02-15'",
    "DATE '2024-03-05'",
    "DATE '2025-01-12'",
    "DATE '2024-03-20'",
    "DATE '2024-04-01'",
    "DATE '2025-02-18'",
    "DATE '2024-04-12'",
    "DATE '2024-05-02'",
    "DATE '2025-04-10'",
    "DATE '2024-05-15'",
    "DATE '2024-05-16'",
    "DATE '2025-07-01'",
    "DATE '2024-06-10'",
    "DATE '2024-06-12'",
    "DATE '2025-10-22'",
    "DATE '2024-07-05'",
    "DATE '2024-07-07'",
    "DATE '2025-09-18'",
    "DATE '2024-08-01'",
    "DATE '2024-08-05'",
    "DATE '2025-01-25'",
    "DATE '2025-02-15'",
    "DATE '2025-02-16'",
    "DATE '2025-11-03'",
    "DATE '2025-11-04'",
    "DATE '2024-09-10'",
    "DATE '2024-09-15'",

    "DATE '2025-12-10'",
    "DATE '2025-12-12'",
    "DATE '2026-01-15'",
    "DATE '2026-02-20'",
    "DATE '2026-03-05'"
]

MATRICOLA_VETERINARIO = [
    "'ESA001'",
    "'ESA002'",
    "'ESA001'",
    "'ESA003'",
    "'ESA002'",
    "'ESA004'",
    "'ESA001'",
    "'ESA003'",
    "'ESA004'",
    "'ESA002'",
    "'ESA002'",
    "'ESA005'",
    "'ESA003'",
    "'ESA003'",
    "'ESA005'",
    "'ESA004'",
    "'ESA004'",
    "'ESA005'",
    "'ESA001'",
    "'ESA001'",
    "'ESA005'",
    "'ESA002'",
    "'ESA002'",
    "'ESA004'",
    "'ESA006'",
    "'ESA006'",
    "'ESA006'",
    "'ESA006'",
    "'ESA003'",
    "'ESA003'",

    "'ESA001'",
    "'ESA002'",
    "'ESA003'",
    "'ESA004'",
    "'ESA006'"
]

STATO_SALUTE = [
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'DISCRETO'",
    "'BUONO'",
    "'DISCRETO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'DISCRETO'",
    "'BUONO'",
    "'BUONO'",
    "'CRITICO'",
    "'BUONO'",
    "'BUONO'",
    "'DISCRETO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'CRITICO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'BUONO'",

    "'BUONO'",
    "'BUONO'",
    "'BUONO'",
    "'DISCRETO'",
    "'BUONO'"
]

TIPO_VISITA = [
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'BIOSICUREZZA'",
    "'BIOSICUREZZA'",
    "'EMERGENZA'",
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'ROUTINE'",
    "'ROUTINE'",
    "'INGRESSO'",
    "'ROUTINE'",
    "'EMERGENZA'",
    "'INGRESSO'",
    "'BIOSICUREZZA'",
    "'BIOSICUREZZA'",
    "'BIOSICUREZZA'",
    "'BIOSICUREZZA'",
    "'ROUTINE'",
    "'ROUTINE'",

    "'ROUTINE'",
    "'ROUTINE'",
    "'BIOSICUREZZA'",
    "'CONTROLLO_GESTAZIONE'",
    "'BIOSICUREZZA'"
]


theList=list(zip(ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA))

keys = ["ETICHETTA_ANIMALE", "DATA_VISITA", "MATRICOLA_VETERINARIO", "STATO_SALUTE", "TIPO_VISITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("VISITA_VETERINARIA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/7_visita_veterinaria.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/7_visita_veterinaria.sql", lines)