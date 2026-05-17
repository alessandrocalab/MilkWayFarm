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


#SERBATOIO:NUMERO_SERBATOIO CODICE_AREA NOME_STRUTTURA DATA_SMONTAGGIO DATA_MONTAGGIO PRESSIONE_MAX_PA DIMENSIONE_M3 

NUMERO_SERBATOIO = [
    "'A001'",
    "'A002'",
    "'A003'",
    "'A004'",
    "'A001'",
    "'A002'",
    "'A001'",
    "'A002'",
    "'A003'",
    "'A001'"
]

CODICE_AREA = [
    "'A12A'",
    "'A12A'",
    "'A12A'",
    "'A12A'",
    "'A05A'",
    "'A06A'",
    "'A11A'",
    "'A11A'",
    "'A16A'",
    "'A07A'"
]

NOME_STRUTTURA = [
    "'Area Serbatoi Eta'",
    "'Area Serbatoi Eta'",
    "'Area Serbatoi Eta'",
    "'Area Serbatoi Eta'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Deposito Tecnico Zeta'",
    "'Deposito Tecnico Zeta'",
    "'Modulo Quarantena Lambda'",
    "'Laboratorio Biologico Delta'"
]

DATA_SMONTAGGIO = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "DATE '2025-10-30'",
    "DATE '2025-10-30'",
    "NULL",
    "NULL"
]

DATA_MONTAGGIO = [
    "DATE '2022-04-10'",
    "DATE '2022-04-12'",
    "DATE '2022-04-15'",
    "DATE '2022-04-18'",
    "DATE '2019-05-10'",
    "DATE '2019-06-20'",
    "DATE '2021-07-20'",
    "DATE '2021-07-25'",
    "DATE '2025-03-15'",
    "DATE '2020-03-15'"
]

PRESSIONE_MAX_PA = [
    300000,   # acqua tecnica
    450000,   # ossigeno/aria compressa
    250000,   # soluzione nutritiva
    500000,   # riserva emergenza
    200000,   # serbatoio idroponico area A05A
    200000,   # serbatoio idroponico area A06A
    350000,   # tecnico dismesso
    350000,   # tecnico dismesso
    250000,   # quarantena
    150000    # laboratorio
]

DIMENSIONE_M3 = [
    80,
    60,
    70,
    50,
    35,
    35,
    45,
    45,
    25,
    15
]


theList=list(zip(NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3))

keys = ["NUMERO_SERBATOIO", "CODICE_AREA", "NOME_STRUTTURA", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "PRESSIONE_MAX_PA", "DIMENSIONE_M3"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3\n"
for i in range(len(theList)):
  lines+=make_DML_line("SERBATOIO", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/5_serbatoio.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/5_serbatoio.sql", lines)