import os
import sys
import json

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

from python.make_DML.core.utils.make_DML_line import make_DML_line
from python.make_DML.core.utils.make_DML import make_DML


#PRODOTTO_CONTIENE_SOSTANZA:NOME_PRODOTTO NOME_SOSTANZA LIVELLO_PRESENZA 

RIGHE_PRODOTTO_SOSTANZA = [
    # LATTE E DERIVATI
    ("'Latte bovino'", "'Lattosio'", "'ALTO'"),
    ("'Latte bovino'", "'Caseina'", "'MEDIO'"),
    ("'Latte bovino'", "'Proteine del siero del latte'", "'MEDIO'"),
    ("'Latte bovino'", "'Albumina sierica bovina'", "'BASSO'"),

    ("'Latte caprino'", "'Lattosio'", "'MEDIO'"),
    ("'Latte caprino'", "'Caseina'", "'MEDIO'"),
    ("'Latte caprino'", "'Proteine del siero del latte'", "'MEDIO'"),

    ("'Latte ovino'", "'Lattosio'", "'MEDIO'"),
    ("'Latte ovino'", "'Caseina'", "'ALTO'"),
    ("'Latte ovino'", "'Proteine del siero del latte'", "'MEDIO'"),

    ("'Formaggio fresco'", "'Lattosio'", "'BASSO'"),
    ("'Formaggio fresco'", "'Caseina'", "'ALTO'"),
    ("'Formaggio fresco'", "'Proteine del siero del latte'", "'MEDIO'"),

    ("'Yogurt naturale'", "'Lattosio'", "'BASSO'"),
    ("'Yogurt naturale'", "'Caseina'", "'MEDIO'"),
    ("'Yogurt naturale'", "'Proteine del siero del latte'", "'BASSO'"),

    ("'Burro'", "'Lattosio'", "'TRACCIA'"),
    ("'Burro'", "'Caseina'", "'TRACCIA'"),

    ("'Panna'", "'Lattosio'", "'BASSO'"),
    ("'Panna'", "'Caseina'", "'BASSO'"),

    # UOVA
    ("'Uova di gallina'", "'Proteine dell uovo'", "'ALTO'"),
    ("'Uova di gallina'", "'Ovoalbumina'", "'ALTO'"),
    ("'Uova di gallina'", "'Ovomucoide'", "'MEDIO'"),

    ("'Uova di quaglia'", "'Proteine dell uovo'", "'ALTO'"),
    ("'Uova di quaglia'", "'Ovoalbumina'", "'ALTO'"),
    ("'Uova di quaglia'", "'Ovomucoide'", "'MEDIO'"),

    # CEREALI
    ("'Grano duro'", "'Glutine'", "'ALTO'"),
    ("'Grano duro'", "'Gliadina'", "'ALTO'"),
    ("'Grano duro'", "'Glutenina'", "'ALTO'"),
    ("'Grano duro'", "'Fruttani'", "'MEDIO'"),

    ("'Farina di grano'", "'Glutine'", "'ALTO'"),
    ("'Farina di grano'", "'Gliadina'", "'ALTO'"),
    ("'Farina di grano'", "'Glutenina'", "'ALTO'"),
    ("'Farina di grano'", "'Fruttani'", "'MEDIO'"),

    ("'Mais'", "'Proteine del mais'", "'MEDIO'"),

    # LEGUMI E SOIA
    ("'Fagiolo'", "'Proteine dei legumi'", "'ALTO'"),
    ("'Fagiolo'", "'Vicilina'", "'MEDIO'"),
    ("'Fagiolo'", "'Lectine vegetali'", "'MEDIO'"),
    ("'Fagiolo'", "'Galatto oligosaccaridi'", "'ALTO'"),
    ("'Fagiolo'", "'Raffinosio'", "'MEDIO'"),
    ("'Fagiolo'", "'Stachiosio'", "'MEDIO'"),

    ("'Ceci'", "'Proteine dei legumi'", "'ALTO'"),
    ("'Ceci'", "'Vicilina'", "'MEDIO'"),
    ("'Ceci'", "'Convicilina'", "'MEDIO'"),
    ("'Ceci'", "'Galatto oligosaccaridi'", "'ALTO'"),
    ("'Ceci'", "'Raffinosio'", "'MEDIO'"),
    ("'Ceci'", "'Stachiosio'", "'MEDIO'"),

    ("'Lenticchie'", "'Proteine dei legumi'", "'ALTO'"),
    ("'Lenticchie'", "'Vicilina'", "'MEDIO'"),
    ("'Lenticchie'", "'Convicilina'", "'MEDIO'"),
    ("'Lenticchie'", "'Galatto oligosaccaridi'", "'MEDIO'"),
    ("'Lenticchie'", "'Raffinosio'", "'MEDIO'"),

    ("'Piselli'", "'Proteine dei legumi'", "'MEDIO'"),
    ("'Piselli'", "'Vicilina'", "'MEDIO'"),
    ("'Piselli'", "'Convicilina'", "'MEDIO'"),

    ("'Soia'", "'Proteine della soia'", "'ALTO'"),
    ("'Soia'", "'Lecitina di soia'", "'MEDIO'"),
    ("'Soia'", "'Nichel alimentare'", "'MEDIO'"),
    ("'Soia'", "'Raffinosio'", "'MEDIO'"),
    ("'Soia'", "'Stachiosio'", "'MEDIO'"),

    # ORTAGGI
    ("'Patata'", "'Solanina'", "'BASSO'"),

    ("'Pomodoro'", "'Salicilati naturali'", "'MEDIO'"),
    ("'Pomodoro'", "'Istamina'", "'BASSO'"),
    ("'Pomodoro'", "'Fruttosio'", "'BASSO'"),

    ("'Lattuga'", "'Salicilati naturali'", "'TRACCIA'"),

    ("'Spinaci'", "'Ossalati'", "'ALTO'"),
    ("'Spinaci'", "'Nichel alimentare'", "'MEDIO'"),

    ("'Carota'", "'Salicilati naturali'", "'BASSO'"),
    ("'Carota'", "'Fruttosio'", "'BASSO'"),

    ("'Zucchina'", "'Salicilati naturali'", "'TRACCIA'"),
    ("'Cetriolo'", "'Salicilati naturali'", "'TRACCIA'"),

    ("'Melanzana'", "'Solanina'", "'BASSO'"),
    ("'Melanzana'", "'Istamina'", "'BASSO'"),
    ("'Melanzana'", "'Salicilati naturali'", "'MEDIO'"),

    ("'Peperone'", "'Capsaicina'", "'BASSO'"),
    ("'Peperone'", "'Salicilati naturali'", "'MEDIO'"),

    # FRUTTA
    ("'Fragola'", "'Fruttosio'", "'MEDIO'"),
    ("'Fragola'", "'Salicilati naturali'", "'MEDIO'"),
    ("'Fragola'", "'Istamina'", "'BASSO'"),

    ("'Mela'", "'Fruttosio'", "'MEDIO'"),
    ("'Pera'", "'Fruttosio'", "'ALTO'"),

    ("'Uva'", "'Fruttosio'", "'ALTO'"),
    ("'Uva'", "'Salicilati naturali'", "'BASSO'"),

    # FUNGHI E ALGHE
    ("'Funghi coltivati'", "'Proteine fungine'", "'MEDIO'"),
    ("'Funghi coltivati'", "'Chitina fungina'", "'ALTO'"),
    ("'Funghi coltivati'", "'Purine'", "'MEDIO'"),

    ("'Alghe alimentari'", "'Ficocianina algale'", "'MEDIO'"),
    ("'Alghe alimentari'", "'Iodio algale'", "'ALTO'"),

    # CARNI
    ("'Carne bovina'", "'Alfa gal'", "'MEDIO'"),
    ("'Carne bovina'", "'Proteine della carne bovina'", "'ALTO'"),
    ("'Carne bovina'", "'Albumina sierica bovina'", "'BASSO'"),

    ("'Carne suina'", "'Alfa gal'", "'MEDIO'"),
    ("'Carne suina'", "'Proteine della carne suina'", "'ALTO'"),

    ("'Carne ovina'", "'Alfa gal'", "'MEDIO'"),
    ("'Carne ovina'", "'Proteine della carne ovina'", "'ALTO'"),

    ("'Carne caprina'", "'Alfa gal'", "'MEDIO'"),
    ("'Carne caprina'", "'Proteine della carne caprina'", "'ALTO'"),

    ("'Carne di pollo'", "'Proteine della carne avicola'", "'ALTO'"),
    ("'Carne di tacchino'", "'Proteine della carne avicola'", "'ALTO'"),

    ("'Carne di coniglio'", "'Proteine della carne di coniglio'", "'ALTO'")
]


NOME_PRODOTTO = [riga[0] for riga in RIGHE_PRODOTTO_SOSTANZA]
NOME_SOSTANZA = [riga[1] for riga in RIGHE_PRODOTTO_SOSTANZA]
LIVELLO_PRESENZA = [riga[2] for riga in RIGHE_PRODOTTO_SOSTANZA]


theList=list(zip(NOME_PRODOTTO, NOME_SOSTANZA, LIVELLO_PRESENZA))

keys = ["NOME_PRODOTTO", "NOME_SOSTANZA", "LIVELLO_PRESENZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_SOSTANZA, LIVELLO_PRESENZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_CONTIENE_SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/3_prodotto_contiene_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/3_prodotto_contiene_sostanza.sql", lines)