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


#PRODOTTO_MISSIONE:NOME_PRODOTTO NOME_MISSIONE QUANTITA DATA_PRODUZIONE 

NOME_PRODOTTO = []

NOME_MISSIONE = []

QUANTITA = []

DATA_PRODUZIONE = []


theList=list(zip(NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE))

keys = ["NOME_PRODOTTO", "NOME_MISSIONE", "QUANTITA", "DATA_PRODUZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_MISSIONE", theList[i])+"\n"

os.makedirs("make_DML/data/5_missione.sql", exist_ok=True)
with open("make_DML/data/5_missione.sql/2_prodotto_missione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/5_missione.sql/2_prodotto_missione.sql", lines)