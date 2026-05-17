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


#SOSTANZA:NOME_SOSTANZA IS_POTENZIALE_ALLERGENE IS_POTENZIALE_INTOLLERANTE 

NOME_SOSTANZA = [
    "'Lattosio'",
    "'Caseina'",
    "'Proteine del latte'",
    "'Albumina'",
    "'Ovomucoide'",
    "'Glutine'",
    "'Frumento'",
    "'Soia'",
    "'Lecitina di soia'",
    "'Mais'",
    "'Solanina'",
    "'Nichel'",
    "'Fruttosio'",
    "'Saccarosio'",
    "'Istamina'",
    "'Beta-glucani'",
    "'Chitina'",
    "'Acido citrico'",
    "'Potassio'",
    "'Fibre vegetali'"
]

IS_POTENZIALE_ALLERGENE = [
    0,  # Lattosio
    1,  # Caseina
    1,  # Proteine del latte
    1,  # Albumina
    1,  # Ovomucoide
    1,  # Glutine
    1,  # Frumento
    1,  # Soia
    1,  # Lecitina di soia
    1,  # Mais
    0,  # Solanina
    1,  # Nichel
    0,  # Fruttosio
    0,  # Saccarosio
    0,  # Istamina
    0,  # Beta-glucani
    1,  # Chitina
    0,  # Acido citrico
    0,  # Potassio
    0   # Fibre vegetali
]

IS_POTENZIALE_INTOLLERANTE = [
    1,  # Lattosio
    0,  # Caseina
    0,  # Proteine del latte
    0,  # Albumina
    0,  # Ovomucoide
    1,  # Glutine
    1,  # Frumento
    0,  # Soia
    0,  # Lecitina di soia
    0,  # Mais
    1,  # Solanina
    1,  # Nichel
    1,  # Fruttosio
    1,  # Saccarosio
    1,  # Istamina
    0,  # Beta-glucani
    0,  # Chitina
    1,  # Acido citrico
    0,  # Potassio
    1   # Fibre vegetali
]


theList=list(zip(NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE))

keys = ["NOME_SOSTANZA", "IS_POTENZIALE_ALLERGENE", "IS_POTENZIALE_INTOLLERANTE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE\n"
for i in range(len(theList)):
  lines+=make_DML_line("SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/2_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/2_sostanza.sql", lines)