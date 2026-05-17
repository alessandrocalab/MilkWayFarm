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


#CELLA_IDROPONICA:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA SISTEMA_IDROPONICO DATA_SMONTAGGIO DATA_MONTAGGIO MAX_COLTURE 

CODICE_CELLA_IDR = [
    "'-001A'",
    "'-002A'",
    "'-003A'",
    "'-004A'",
    "'-005A'",
    "'-006A'",
    "'-007A'",
    "'-008A'",
    "'-009A'",
    "'-010A'",
    "'-011A'",
    "'-012A'"
]

CODICE_AREA = [
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A06A'",
    "'A06A'",
    "'A06A'",
    "'A06A'",
    "'A06A'",
    "'A06A'"
]

NOME_STRUTTURA = [
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'"
]

SISTEMA_IDROPONICO = [
    "'NFT'",
    "'NFT'",
    "'DWC'",
    "'DWC'",
    "'AEROPONICO'",
    "'GOCCIA'",
    "'NFT'",
    "'DWC'",
    "'AEROPONICO'",
    "'GOCCIA'",
    "'SUBSTRATO_INERTE'",
    "'SUBSTRATO_INERTE'"
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
    "NULL",
    "NULL",
    "NULL"
]

DATA_MONTAGGIO = [
    "DATE '2019-05-15'",
    "DATE '2019-05-18'",
    "DATE '2019-05-22'",
    "DATE '2019-05-25'",
    "DATE '2019-06-01'",
    "DATE '2019-06-05'",
    "DATE '2019-06-20'",
    "DATE '2019-06-23'",
    "DATE '2019-06-28'",
    "DATE '2019-07-02'",
    "DATE '2019-07-08'",
    "DATE '2019-07-12'"
]

MAX_COLTURE = [
    120,  # NFT lattuga / colture leggere
    120,  # NFT lattuga / erbe
    80,   # DWC colture a foglia
    80,   # DWC colture a foglia
    60,   # aeroponico pomodoro / fragola
    50,   # goccia patata / carota
    100,  # NFT seconda area
    75,   # DWC seconda area
    55,   # aeroponico seconda area
    45,   # goccia seconda area
    65,   # substrato inerte
    65    # substrato inerte
]


theList=list(zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE))

keys = ["CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "SISTEMA_IDROPONICO", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "MAX_COLTURE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE\n"
for i in range(len(theList)):
  lines+=make_DML_line("CELLA_IDROPONICA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/9_cella_idroponica.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/9_cella_idroponica.sql", lines)