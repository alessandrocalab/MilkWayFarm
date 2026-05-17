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


#MISSIONE_RIFORNIMENTO:NOME_MISSIONE DATA_LANCIO DATA_ARRIVO_PREVISTO DATA_ARRIVO_EFFETTIVO VOLUME_RIFORNIMENTO_M3 MASSA_RIFORNIMENTO_KG BASE_PARTENZA 

NOME_MISSIONE = []

DATA_LANCIO = []

DATA_ARRIVO_PREVISTO = []

DATA_ARRIVO_EFFETTIVO = []

VOLUME_RIFORNIMENTO_M3 = []

MASSA_RIFORNIMENTO_KG = []

BASE_PARTENZA = []


theList=list(zip(NOME_MISSIONE, DATA_LANCIO, DATA_ARRIVO_PREVISTO, DATA_ARRIVO_EFFETTIVO, VOLUME_RIFORNIMENTO_M3, MASSA_RIFORNIMENTO_KG, BASE_PARTENZA))

keys = ["NOME_MISSIONE", "DATA_LANCIO", "DATA_ARRIVO_PREVISTO", "DATA_ARRIVO_EFFETTIVO", "VOLUME_RIFORNIMENTO_M3", "MASSA_RIFORNIMENTO_KG", "BASE_PARTENZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_MISSIONE, DATA_LANCIO, DATA_ARRIVO_PREVISTO, DATA_ARRIVO_EFFETTIVO, VOLUME_RIFORNIMENTO_M3, MASSA_RIFORNIMENTO_KG, BASE_PARTENZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("MISSIONE_RIFORNIMENTO", theList[i])+"\n"

os.makedirs("make_DML/data/5_missione.sql", exist_ok=True)
with open("make_DML/data/5_missione.sql/1_missione_rifornimento.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/5_missione.sql/1_missione_rifornimento.sql", lines)