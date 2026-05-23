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


#TIPO_COLTURA:NOME_TIPO_COLTURA CATEGORIA_COLTURA DURATA_CICLO_COLTURA_GIORNI 

NOME_TIPO_COLTURA = []

CATEGORIA_COLTURA = []

DURATA_CICLO_COLTURA_GIORNI = []


theList=list(zip(NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI))

keys = ["NOME_TIPO_COLTURA", "CATEGORIA_COLTURA", "DURATA_CICLO_COLTURA_GIORNI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_COLTURA", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/2_tipo_coltura.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/2_tipo_coltura.SQL", lines)