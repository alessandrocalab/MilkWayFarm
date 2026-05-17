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


#STRUTTURA:NOME_STRUTTURA DATA_TERMINAZIONE QUOTA LONGITUDINE LATITUDINE VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

NOME_STRUTTURA = [
    "'Base Selene Centrale'",
    "'Modulo Agricolo Alfa'",
    "'Modulo Zootecnico Beta'",
    "'Serra Idroponica Gamma'",
    "'Laboratorio Biologico Delta'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Tecnico Zeta'",
    "'Area Serbatoi Eta'",
    "'Modulo Energia Theta'",
    "'Centro Controllo Iota'",
    "'Cupola Osservazione Kappa'",
    "'Modulo Quarantena Lambda'"
]

DATA_TERMINAZIONE = [
    "NULL",              # Base Selene Centrale - ancora attiva
    "NULL",              # Modulo Agricolo Alfa - ancora attivo
    "NULL",              # Modulo Zootecnico Beta - ancora attivo
    "NULL",              # Serra Idroponica Gamma - ancora attiva
    "NULL",              # Laboratorio Biologico Delta - ancora attivo
    "NULL",              # Deposito Alimentare Epsilon - ancora attivo
    "DATE '2025-10-30'", # Deposito Tecnico Zeta - dismesso
    "NULL",              # Area Serbatoi Eta - ancora attiva
    "NULL",              # Modulo Energia Theta - ancora attivo
    "NULL",              # Centro Controllo Iota - ancora attivo
    "NULL",              # Cupola Osservazione Kappa - ancora attiva
    "NULL"               # Modulo Quarantena Lambda - ancora attivo
]

QUOTA = [
    2100,  # Base Selene Centrale
    2085,  # Modulo Agricolo Alfa
    2078,  # Modulo Zootecnico Beta
    2092,  # Serra Idroponica Gamma
    2110,  # Laboratorio Biologico Delta
    2065,  # Deposito Alimentare Epsilon
    2058,  # Deposito Tecnico Zeta
    2049,  # Area Serbatoi Eta
    2135,  # Modulo Energia Theta
    2120,  # Centro Controllo Iota
    2160,  # Cupola Osservazione Kappa
    2070   # Modulo Quarantena Lambda
]

LONGITUDINE = [
    0.0012,
    0.0021,
    0.0034,
    0.0048,
    0.0060,
    -0.0015,
    -0.0028,
    -0.0040,
    0.0085,
    0.0000,
    0.0102,
    -0.0063
]

LATITUDINE = [
    -89.9001,
    -89.8994,
    -89.8987,
    -89.8979,
    -89.8972,
    -89.9008,
    -89.9015,
    -89.9021,
    -89.8968,
    -89.8999,
    -89.8955,
    -89.9030
]

VOLUME_M3 = [
    18000,  # Base Selene Centrale
    9500,   # Modulo Agricolo Alfa
    7800,   # Modulo Zootecnico Beta
    12000,  # Serra Idroponica Gamma
    5200,   # Laboratorio Biologico Delta
    6000,   # Deposito Alimentare Epsilon
    4300,   # Deposito Tecnico Zeta
    3500,   # Area Serbatoi Eta
    7000,   # Modulo Energia Theta
    4800,   # Centro Controllo Iota
    2600,   # Cupola Osservazione Kappa
    3000    # Modulo Quarantena Lambda
]

SUPERFICIE_MQ = [
    4200,  # Base Selene Centrale
    2600,  # Modulo Agricolo Alfa
    2100,  # Modulo Zootecnico Beta
    3200,  # Serra Idroponica Gamma
    1400,  # Laboratorio Biologico Delta
    1800,  # Deposito Alimentare Epsilon
    1500,  # Deposito Tecnico Zeta
    1300,  # Area Serbatoi Eta
    2200,  # Modulo Energia Theta
    1200,  # Centro Controllo Iota
    900,   # Cupola Osservazione Kappa
    1000   # Modulo Quarantena Lambda
]

DATA_ATTIVAZIONE = [
    "DATE '2017-03-15'",  # Base Selene Centrale
    "DATE '2018-01-20'",  # Modulo Agricolo Alfa
    "DATE '2018-09-05'",  # Modulo Zootecnico Beta
    "DATE '2019-04-12'",  # Serra Idroponica Gamma
    "DATE '2020-02-18'",  # Laboratorio Biologico Delta
    "DATE '2020-11-30'",  # Deposito Alimentare Epsilon
    "DATE '2021-06-22'",  # Deposito Tecnico Zeta
    "DATE '2022-03-10'",  # Area Serbatoi Eta
    "DATE '2022-12-01'",  # Modulo Energia Theta
    "DATE '2023-07-15'",  # Centro Controllo Iota
    "DATE '2024-05-08'",  # Cupola Osservazione Kappa
    "DATE '2025-02-14'"   # Modulo Quarantena Lambda
]


theList=list(zip(NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["NOME_STRUTTURA", "DATA_TERMINAZIONE", "QUOTA", "LONGITUDINE", "LATITUDINE", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("STRUTTURA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/1_struttura.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/1_struttura.sql", lines)