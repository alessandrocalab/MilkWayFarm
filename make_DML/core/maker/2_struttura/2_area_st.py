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


#AREA_ST:CODICE_AREA NOME_STRUTTURA DATA_TERMINAZIONE TEMPERATURA_MIN TEMPERATURA_MAX UMIDITA_MIN UMIDITA_MAX LIVELLO_SICUREZZA PRESSIONE_PA VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

CODICE_AREA = [
    "'A01A'",
    "'A02A'",
    "'A03A'",
    "'A04A'",
    "'A05A'",
    "'A06A'",
    "'A07A'",
    "'A08A'",
    "'A09A'",
    "'A10A'",
    "'A11A'",
    "'A12A'",
    "'A13A'",
    "'A14A'",
    "'A15A'",
    "'A16A'"
]

NOME_STRUTTURA = [
    "'Modulo Agricolo Alfa'",
    "'Modulo Agricolo Alfa'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Laboratorio Biologico Delta'",
    "'Laboratorio Biologico Delta'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Tecnico Zeta'",
    "'Area Serbatoi Eta'",
    "'Modulo Energia Theta'",
    "'Centro Controllo Iota'",
    "'Cupola Osservazione Kappa'",
    "'Modulo Quarantena Lambda'"
]

DATA_TERMINAZIONE = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "DATE '2025-10-30'",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

TEMPERATURA_MIN = [
    291.15,  # 18°C
    288.15,  # 15°C
    289.15,  # 16°C
    291.15,  # 18°C
    293.15,  # 20°C
    291.15,  # 18°C
    291.15,  # 18°C
    287.15,  # 14°C
    275.15,  # 2°C
    283.15,  # 10°C
    278.15,  # 5°C
    278.15,  # 5°C
    285.15,  # 12°C
    291.15,  # 18°C
    289.15,  # 16°C
    291.15   # 18°C
]

TEMPERATURA_MAX = [
    299.15,  # 26°C
    296.15,  # 23°C
    298.15,  # 25°C
    297.15,  # 24°C
    301.15,  # 28°C
    299.15,  # 26°C
    295.15,  # 22°C
    291.15,  # 18°C
    281.15,  # 8°C
    298.15,  # 25°C
    298.15,  # 25°C
    298.15,  # 25°C
    303.15,  # 30°C
    296.15,  # 23°C
    295.15,  # 22°C
    296.15   # 23°C
]

UMIDITA_MIN = [
    45,
    35,
    50,
    55,
    70,
    75,
    35,
    30,
    50,
    20,
    20,
    20,
    20,
    35,
    30,
    40
]

UMIDITA_MAX = [
    70,
    60,
    75,
    80,
    90,
    95,
    60,
    50,
    80,
    50,
    60,
    60,
    55,
    60,
    55,
    65
]

LIVELLO_SICUREZZA = [
    "'L1'",  # A01A - area agricola
    "'L1'",  # A02A - area agricola
    "'L2'",  # A03A - area zootecnica
    "'L2'",  # A04A - area zootecnica
    "'L1'",  # A05A - idroponica
    "'L1'",  # A06A - idroponica
    "'L3'",  # A07A - laboratorio biologico
    "'L3'",  # A08A - laboratorio biologico/osservazione
    "'L1'",  # A09A - deposito alimentare
    "'L1'",  # A10A - deposito secco
    "'L2'",  # A11A - deposito tecnico
    "'L2'",  # A12A - area serbatoi
    "'L3'",  # A13A - energia
    "'L2'",  # A14A - centro controllo
    "'L0'",  # A15A - osservazione
    "'L3'"   # A16A - quarantena
]

PRESSIONE_PA = [
    101325,
    95000,
    101325,
    101325,
    90000,
    90000,
    101325,
    101325,
    101325,
    95000,
    95000,
    90000,
    85000,
    101325,
    95000,
    101325
]

VOLUME_M3 = [
    1800,
    1200,
    1500,
    1300,
    2200,
    1800,
    900,
    700,
    1100,
    900,
    1000,
    1600,
    1800,
    850,
    600,
    750
]

SUPERFICIE_MQ = [
    520,
    380,
    450,
    400,
    700,
    620,
    280,
    220,
    350,
    300,
    340,
    500,
    600,
    260,
    180,
    240
]

DATA_ATTIVAZIONE = [
    "DATE '2018-02-10'",  # Modulo Agricolo Alfa
    "DATE '2018-03-05'",  # Modulo Agricolo Alfa
    "DATE '2018-10-01'",  # Modulo Zootecnico Beta
    "DATE '2018-11-15'",  # Modulo Zootecnico Beta
    "DATE '2019-05-01'",  # Serra Idroponica Gamma
    "DATE '2019-06-10'",  # Serra Idroponica Gamma
    "DATE '2020-03-01'",  # Laboratorio Biologico Delta
    "DATE '2020-03-20'",  # Laboratorio Biologico Delta
    "DATE '2020-12-15'",  # Deposito Alimentare Epsilon
    "DATE '2021-01-10'",  # Deposito Alimentare Epsilon
    "DATE '2021-07-05'",  # Deposito Tecnico Zeta
    "DATE '2022-04-01'",  # Area Serbatoi Eta
    "DATE '2023-01-10'",  # Modulo Energia Theta
    "DATE '2023-08-01'",  # Centro Controllo Iota
    "DATE '2024-06-01'",  # Cupola Osservazione Kappa
    "DATE '2025-03-01'"   # Modulo Quarantena Lambda
]


theList=list(zip(CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["CODICE_AREA", "NOME_STRUTTURA", "DATA_TERMINAZIONE", "TEMPERATURA_MIN", "TEMPERATURA_MAX", "UMIDITA_MIN", "UMIDITA_MAX", "LIVELLO_SICUREZZA", "PRESSIONE_PA", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("AREA_ST", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/2_area_st.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/2_area_st.sql", lines)