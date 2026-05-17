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


#PRODUZIONE_ANIMALE:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA CODICE_AREA NOME_PRODOTTO QUANTITA 

DATA_PRODUZIONE = [
    "DATE '2024-01-10'",
    "DATE '2024-01-17'",
    "DATE '2024-02-05'",
    "DATE '2024-02-12'",
    "DATE '2024-03-08'",
    "DATE '2024-03-15'",
    "DATE '2024-04-02'",
    "DATE '2024-04-09'",
    "DATE '2024-05-04'",
    "DATE '2024-05-11'",
    "DATE '2024-06-06'",
    "DATE '2024-06-13'",
    "DATE '2024-07-03'",
    "DATE '2024-07-10'",
    "DATE '2024-08-01'",
    "DATE '2024-08-08'",
    "DATE '2024-09-05'",
    "DATE '2024-09-12'",
    "DATE '2024-10-03'",
    "DATE '2024-10-10'",
    "DATE '2024-11-07'",
    "DATE '2024-11-14'",
    "DATE '2024-12-04'",
    "DATE '2024-12-11'",
    "DATE '2025-01-09'",
    "DATE '2025-01-16'",
    "DATE '2025-02-06'",
    "DATE '2025-02-13'",
    "DATE '2025-03-06'",
    "DATE '2025-03-13'"
]

NUMERO_BLOCCO = [
    "'0001'",
    "'0001'",
    "'0001'",
    "'0001'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0001'",
    "'0001'",
    "'0001'",
    "'0001'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0001'",
    "'0001'",
    "'0001'",
    "'0001'",
    "'0003'",
    "'0003'",
    "'0003'",
    "'0003'",
    "'0001'",
    "'0001'",
    "'0002'",
    "'0002'",
    "'0001'",
    "'0001'"
]

NOME_STRUTTURA = [
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",
    "'Laboratorio Biologico Delta'",
    "'Laboratorio Biologico Delta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'"
]

CODICE_AREA = [
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A04A'",
    "'A03A'",
    "'A03A'",
    "'A04A'",
    "'A04A'",
    "'A16A'",
    "'A16A'",
    "'A16A'",
    "'A16A'",
    "'A08A'",
    "'A08A'",
    "'A04A'",
    "'A04A'",
    "'A03A'",
    "'A03A'"
]

NOME_PRODOTTO = [
    "'Latte bovino liofilizzato'",
    "'Latte bovino liofilizzato'",
    "'Latte bovino liofilizzato'",
    "'Yogurt liofilizzato'",
    "'Latte bovino liofilizzato'",
    "'Latte bovino liofilizzato'",
    "'Yogurt liofilizzato'",
    "'Latte bovino liofilizzato'",

    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Uova in polvere'",

    "'Latte bovino liofilizzato'",
    "'Yogurt liofilizzato'",
    "'Uova in polvere'",
    "'Uova in polvere'",

    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Latte bovino liofilizzato'",
    "'Yogurt liofilizzato'",

    "'Yogurt liofilizzato'",
    "'Yogurt liofilizzato'",

    "'Uova in polvere'",
    "'Uova in polvere'",
    "'Latte bovino liofilizzato'",
    "'Yogurt liofilizzato'"
]

QUANTITA = [
    18.50,
    19.20,
    17.80,
    6.50,
    7.20,
    7.80,
    3.20,
    8.10,

    4.80,
    5.10,
    4.60,
    5.30,
    1.60,
    1.70,
    2.40,
    2.50,

    18.90,
    6.80,
    4.90,
    1.80,

    1.20,
    1.30,
    2.80,
    1.10,

    4.50,
    4.70,

    2.70,
    2.90,
    20.10,
    7.00
]


theList=list(zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, NOME_PRODOTTO, QUANTITA))

keys = ["DATA_PRODUZIONE", "NUMERO_BLOCCO", "NOME_STRUTTURA", "CODICE_AREA", "NOME_PRODOTTO", "QUANTITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, NOME_PRODOTTO, QUANTITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/9_produzione_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/9_produzione_animale.sql", lines)