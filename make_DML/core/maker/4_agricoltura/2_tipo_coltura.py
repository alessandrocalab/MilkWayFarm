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



theDict=zip(NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI)
theList=list(theDict)

lines="--NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI"
for i in range(len(theList)):
   lines+=make_DML_line("TIPO_COLTURA", theList[i])+"\n"
with open("make_DML/data/json", "w", encoding="utf-8") as f:
   json.dump(theDict, f, indent=4, ensure_ascii=False)

make_DML("DB/DML4_agricoltura/2_tipo_coltura.SQL", lines)