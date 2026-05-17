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


#TIPO_PRODOTTO:NOME_PRODOTTO ALCOL FIBRE PROTEINE GRASSI CARBOIDRATI UNITA_MISURA IS_EDIBILE 

NOME_PRODOTTO = [
    # Alimentari
    "'Latte bovino liofilizzato'",
    "'Uova in polvere'",
    "'Farina di grano idroponico'",
    "'Lattuga idroponica'",
    "'Pomodoro idroponico'",
    "'Patata coltivata in serra'",
    "'Soia essiccata'",
    "'Mais essiccato'",
    "'Carota idroponica'",
    "'Fragola idroponica'",
    "'Funghi coltivati'",
    "'Yogurt liofilizzato'",

    # Farmaci per animali
    "'Antibiotico veterinario base'",
    "'Antiparassitario veterinario'",
    "'Vaccino bovino standard'",
    "'Integratore minerale per animali'",
    "'Disinfettante per stalla'",

    # Soluzioni nutritive per piante
    "'Soluzione nutritiva idroponica universale'",
    "'Soluzione nutritiva azotata'",
    "'Soluzione nutritiva fosfo-potassica'",
    "'Correttore PH per colture'",
    "'Chelato di ferro per piante'",

    # Semi
    "'Semi di lattuga'",
    "'Semi di pomodoro'",
    "'Semi di grano'",
    "'Semi di soia'",
    "'Semi di mais'",
    "'Semi di carota'",
    "'Semi di fragola'"
]

ALCOL = [
    # Alimentari
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

    # Farmaci
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Soluzioni nutritive
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Semi
    "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"
]

FIBRE = [
    # Alimentari
    0, 0, 3.4, 1.3, 1.2, 2.2, 9.3, 7.3, 2.8, 2.0, 2.5, 0,

    # Farmaci
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Soluzioni nutritive
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Semi
    "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"
]

PROTEINE = [
    # Alimentari
    26.0, 48.0, 12.0, 1.4, 0.9, 2.0, 36.0, 9.0, 0.9, 0.7, 3.1, 35.0,

    # Farmaci
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Soluzioni nutritive
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Semi
    "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"
]

GRASSI = [
    # Alimentari
    27.0, 40.0, 1.5, 0.2, 0.2, 0.1, 20.0, 4.7, 0.2, 0.3, 0.3, 20.0,

    # Farmaci
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Soluzioni nutritive
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Semi
    "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"
]

CARBOIDRATI = [
    # Alimentari
    38.0, 2.0, 72.0, 2.9, 3.9, 17.0, 30.0, 74.0, 9.6, 7.7, 3.3, 38.0,

    # Farmaci
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Soluzioni nutritive
    "NULL", "NULL", "NULL", "NULL", "NULL",

    # Semi
    "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"
]

UNITA_MISURA = [
    # Alimentari
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",

    # Farmaci
    "'ml'",
    "'ml'",
    "'dose'",
    "'kg'",
    "'l'",

    # Soluzioni nutritive
    "'l'",
    "'l'",
    "'l'",
    "'l'",
    "'kg'",

    # Semi
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'",
    "'kg'"
]

IS_EDIBILE = [
    # Alimentari
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

    # Farmaci
    0, 0, 0, 0, 0,

    # Soluzioni nutritive
    0, 0, 0, 0, 0,

    # Semi
    0, 0, 0, 0, 0, 0, 0
]


theList=list(zip(NOME_PRODOTTO, ALCOL, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE))

keys = ["NOME_PRODOTTO", "ALCOL", "FIBRE", "PROTEINE", "GRASSI", "CARBOIDRATI", "UNITA_MISURA", "IS_EDIBILE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, ALCOL, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_PRODOTTO", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/1_tipo_prodotto.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/1_tipo_prodotto.sql", lines)