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


#MODALITA_CONSERVAZIONE:NOME_CONSERVAZIONE DURATA_MASSIMA_GIORNI TEMPERATURA_MAX TEMPERATURA_MIN UMIDITA_MIN UMIDITA_MAX 

NOME_CONSERVAZIONE = [
    "'Ambiente controllato secco'",
    "'Refrigerazione standard'",
    "'Congelamento profondo'",
    "'Liofilizzato sigillato'",
    "'Serra idroponica fresca'",
    "'Deposito farmaci veterinari'",
    "'Deposito soluzioni nutritive'",
    "'Deposito semi secco'",
    "'Deposito chimico tecnico'"
]

DURATA_MASSIMA_GIORNI = [
    365,   # Ambiente controllato secco
    14,    # Refrigerazione standard
    730,   # Congelamento profondo
    1095,  # Liofilizzato sigillato
    7,     # Serra idroponica fresca
    365,   # Deposito farmaci veterinari
    180,   # Deposito soluzioni nutritive
    730,   # Deposito semi secco
    365    # Deposito chimico tecnico
]

TEMPERATURA_MAX = [
    298.15,  # 25°C
    277.15,  # 4°C
    255.15,  # -18°C
    298.15,  # 25°C
    285.15,  # 12°C
    298.15,  # 25°C
    298.15,  # 25°C
    288.15,  # 15°C
    298.15   # 25°C
]

TEMPERATURA_MIN = [
    288.15,  # 15°C
    273.15,  # 0°C
    243.15,  # -30°C
    283.15,  # 10°C
    275.15,  # 2°C
    288.15,  # 15°C
    278.15,  # 5°C
    278.15,  # 5°C
    278.15   # 5°C
]

UMIDITA_MIN = [
    20,  # Ambiente controllato secco
    50,  # Refrigerazione standard
    30,  # Congelamento profondo
    10,  # Liofilizzato sigillato
    85,  # Serra idroponica fresca
    30,  # Deposito farmaci veterinari
    20,  # Deposito soluzioni nutritive
    10,  # Deposito semi secco
    20   # Deposito chimico tecnico
]

UMIDITA_MAX = [
    50,  # Ambiente controllato secco
    80,  # Refrigerazione standard
    60,  # Congelamento profondo
    30,  # Liofilizzato sigillato
    95,  # Serra idroponica fresca
    60,  # Deposito farmaci veterinari
    60,  # Deposito soluzioni nutritive
    40,  # Deposito semi secco
    60   # Deposito chimico tecnico
]


theList=list(zip(NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX))

keys = ["NOME_CONSERVAZIONE", "DURATA_MASSIMA_GIORNI", "TEMPERATURA_MAX", "TEMPERATURA_MIN", "UMIDITA_MIN", "UMIDITA_MAX"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX\n"
for i in range(len(theList)):
  lines+=make_DML_line("MODALITA_CONSERVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/3_modalita_conservazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/3_modalita_conservazione.sql", lines)