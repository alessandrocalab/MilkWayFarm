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


#SCAFFALE:NUMERO_SCAFFALE CODICE_AREA NOME_STRUTTURA DATA_SMONTAGGIO DATA_MONTAGGIO CAPACITA_KG DIMENSIONE_M3 

NUMERO_SCAFFALE = [
    "'0001'",
    "'0002'",
    "'0003'",
    "'0004'",
    "'0001'",
    "'0002'",
    "'0003'",
    "'0001'",
    "'0002'",
    "'0001'",
    "'0002'",
    "'0001'"
]

CODICE_AREA = [
    "'A09A'",
    "'A09A'",
    "'A09A'",
    "'A09A'",
    "'A10A'",
    "'A10A'",
    "'A10A'",
    "'A07A'",
    "'A07A'",
    "'A11A'",
    "'A11A'",
    "'A16A'"
]

NOME_STRUTTURA = [
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Laboratorio Biologico Delta'",
    "'Laboratorio Biologico Delta'",
    "'Deposito Tecnico Zeta'",
    "'Deposito Tecnico Zeta'",
    "'Modulo Quarantena Lambda'"
]

DATA_SMONTAGGIO = [
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
    "DATE '2025-10-30'",
    "NULL"
]

DATA_MONTAGGIO = [
    "DATE '2020-12-20'",
    "DATE '2020-12-21'",
    "DATE '2020-12-22'",
    "DATE '2020-12-23'",
    "DATE '2021-01-15'",
    "DATE '2021-01-16'",
    "DATE '2021-01-17'",
    "DATE '2020-03-10'",
    "DATE '2020-03-12'",
    "DATE '2021-07-15'",
    "DATE '2021-07-18'",
    "DATE '2025-03-10'"
]

CAPACITA_KG = [
    1200,
    1200,
    1000,
    1000,
    800,
    800,
    600,
    250,
    250,
    700,
    700,
    300
]

DIMENSIONE_M3 = [
    18,
    18,
    15,
    15,
    12,
    12,
    10,
    5,
    5,
    14,
    14,
    6
]


theList=list(zip(NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3))

keys = ["NUMERO_SCAFFALE", "CODICE_AREA", "NOME_STRUTTURA", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "CAPACITA_KG", "DIMENSIONE_M3"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, CAPACITA_KG, DIMENSIONE_M3\n"
for i in range(len(theList)):
  lines+=make_DML_line("SCAFFALE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/4_scaffale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/4_scaffale.sql", lines)