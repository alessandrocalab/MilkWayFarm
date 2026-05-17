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


#REGISTRAZIONE_SENSORE:SERIALE DATA_SECONDI NOME_PRODUTTORE MISURAZIONE 

SERIALE = [
    "'SEN000001'",
    "'SEN000001'",
    "'SEN000002'",
    "'SEN000002'",
    "'SEN000003'",
    "'SEN000003'",

    "'SEN000004'",
    "'SEN000004'",
    "'SEN000005'",
    "'SEN000005'",
    "'SEN000006'",
    "'SEN000006'",

    "'SEN000007'",
    "'SEN000007'",
    "'SEN000008'",
    "'SEN000008'",
    "'SEN000009'",
    "'SEN000009'",
    "'SEN000010'",
    "'SEN000010'",

    "'SEN000013'",
    "'SEN000013'",
    "'SEN000014'",
    "'SEN000014'",
    "'SEN000015'",
    "'SEN000015'",
    "'SEN000016'",
    "'SEN000016'",
    "'SEN000017'",
    "'SEN000017'",
    "'SEN000018'",
    "'SEN000018'",

    "'SEN000019'",
    "'SEN000019'",
    "'SEN000020'",
    "'SEN000020'",
    "'SEN000021'",
    "'SEN000021'",
    "'SEN000022'",
    "'SEN000022'",
    "'SEN000023'",
    "'SEN000023'",

    "'SEN000024'",
    "'SEN000024'",
    "'SEN000025'",
    "'SEN000025'",
    "'SEN000026'",
    "'SEN000026'",
    "'SEN000027'",
    "'SEN000027'",
    "'SEN000028'",
    "'SEN000028'",

    "'SEN000029'",
    "'SEN000029'",
    "'SEN000030'",
    "'SEN000030'",
    "'SEN000031'",
    "'SEN000031'",
    "'SEN000032'",
    "'SEN000032'"
]

DATA_SECONDI = [
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",

    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'",
    "DATE '2026-05-10'",
    "DATE '2026-05-11'"
]

NOME_PRODUTTORE = [
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",

    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",

    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",

    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'AgriMoon Devices'",
    "'AgriMoon Devices'",

    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",

    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",

    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'"
]

MISURAZIONE = [
    295.45,    # SEN000001 temperatura area agricola
    295.80,
    58.20,     # SEN000002 umidità area agricola
    57.40,
    94980,     # SEN000003 pressione area agricola
    95020,

    820,       # SEN000004 CO2 zootecnia
    870,
    20.70,     # SEN000005 O2 zootecnia
    20.60,
    18.50,     # SEN000006 NH3 zootecnia
    21.30,

    294.20,    # SEN000007 temperatura area zootecnica
    294.60,
    66.50,     # SEN000008 umidità area zootecnica
    67.10,
    310.25,    # SEN000009 temperatura biologica laboratorio
    310.10,
    45.80,     # SEN000010 umidità laboratorio
    46.20,

    6.20,      # SEN000013 pH soluzione idroponica
    6.35,
    1.80,      # SEN000014 conducibilità elettrica
    1.95,
    293.40,    # SEN000015 temperatura liquido
    293.70,
    42000,     # SEN000016 lux
    43500,
    650,       # SEN000017 PAR
    675,
    72.30,     # SEN000018 umidità substrato
    73.10,

    6.10,      # SEN000019 pH seconda area idroponica
    6.25,
    2.10,      # SEN000020 EC seconda area idroponica
    2.05,
    68.50,     # SEN000021 livello serbatoio
    66.80,
    1250.50,   # SEN000022 massa serbatoio
    1242.00,
    42.30,     # SEN000023 portata liquido
    41.90,

    18500,     # SEN000024 potenza elettrica
    19200,
    820.50,    # SEN000025 massa scaffale deposito
    818.30,
    74.20,     # SEN000026 livello scaffale/deposito
    73.80,
    286.20,    # SEN000027 temperatura deposito secco
    286.60,
    36.40,     # SEN000028 umidità deposito secco
    37.10,

    20.80,     # SEN000029 ossigeno centro controllo
    20.70,
    0.35,      # SEN000030 vibrazione modulo energia
    0.42,
    2.10,      # SEN000031 UV cupola osservazione
    2.40,
    0.18,      # SEN000032 radiazione centro controllo
    0.21
]


theList=list(zip(SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE))

keys = ["SERIALE", "DATA_SECONDI", "NOME_PRODUTTORE", "MISURAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("REGISTRAZIONE_SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/8_registrazione_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/8_registrazione_sensore.sql", lines)