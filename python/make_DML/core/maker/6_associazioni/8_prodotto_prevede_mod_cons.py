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


#PRODOTTO_PREVEDE_MOD_CONS:NOME_CONSERVAZIONE NOME_PRODOTTO 

CONSERVAZIONE_PRODOTTO = {
    # LATTE E DERIVATI
    "'Latte bovino'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Latte caprino'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Latte ovino'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Formaggio fresco'": [
        "'Refrigerazione standard'"
    ],
    "'Yogurt naturale'": [
        "'Refrigerazione standard'"
    ],
    "'Burro'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Panna'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],

    # UOVA
    "'Uova di gallina'": [
        "'Refrigerazione standard'"
    ],
    "'Uova di quaglia'": [
        "'Refrigerazione standard'"
    ],

    # CARNI
    "'Carne bovina'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne suina'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne ovina'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne caprina'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne di pollo'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne di tacchino'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],
    "'Carne di coniglio'": [
        "'Refrigerazione standard'",
        "'Congelamento standard'"
    ],

    # CEREALI, FARINE, LEGUMI SECCHI
    "'Grano duro'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Farina di grano'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Mais'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Fagiolo'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Ceci'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Lenticchie'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Piselli'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],
    "'Soia'": [
        "'Ambiente secco controllato'",
        "'Ambiente fresco controllato'"
    ],

    # TUBERI, RADICI, VERDURE E FRUTTA
    "'Patata'": [
        "'Conservazione tuberi e radici'",
        "'Ambiente fresco controllato'"
    ],
    "'Carota'": [
        "'Conservazione tuberi e radici'",
        "'Conservazione verdure fresche'"
    ],
    "'Pomodoro'": [
        "'Conservazione verdure fresche'",
        "'Ambiente fresco controllato'"
    ],
    "'Lattuga'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Spinaci'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Zucchina'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Cetriolo'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Melanzana'": [
        "'Conservazione verdure fresche'",
        "'Ambiente fresco controllato'"
    ],
    "'Peperone'": [
        "'Conservazione verdure fresche'",
        "'Ambiente fresco controllato'"
    ],
    "'Fragola'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Mela'": [
        "'Ambiente fresco controllato'",
        "'Conservazione verdure fresche'"
    ],
    "'Pera'": [
        "'Ambiente fresco controllato'",
        "'Conservazione verdure fresche'"
    ],
    "'Uva'": [
        "'Ambiente fresco controllato'",
        "'Conservazione verdure fresche'"
    ],

    # FUNGHI E ALGHE
    "'Funghi coltivati'": [
        "'Conservazione verdure fresche'",
        "'Refrigerazione standard'"
    ],
    "'Alghe alimentari'": [
        "'Refrigerazione standard'",
        "'Ambiente secco controllato'"
    ],

    # SEMI, SPORE, TALEE
    "'Semi di grano duro'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di mais'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di pomodoro'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di lattuga'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di spinaci'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di carota'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di zucchina'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di cetriolo'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di peperone'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di fagiolo'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di ceci'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di lenticchie'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Semi di soia'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Spore di funghi coltivati'": [
        "'Conservazione semi breve termine'",
        "'Conservazione semi lungo termine'"
    ],
    "'Talee di patata'": [
        "'Conservazione tuberi e radici'",
        "'Conservazione semi breve termine'"
    ],

    # PRODOTTI AGRICOLI TECNICI
    "'Soluzione nutritiva idroponica base'": [
        "'Conservazione soluzioni agricole'",
        "'Ambiente fresco controllato'"
    ],
    "'Soluzione nutritiva concentrata'": [
        "'Conservazione soluzioni agricole'",
        "'Ambiente fresco controllato'"
    ],
    "'Correttore pH acido'": [
        "'Conservazione soluzioni agricole'",
        "'Ambiente fresco controllato'"
    ],
    "'Correttore pH basico'": [
        "'Conservazione soluzioni agricole'",
        "'Ambiente fresco controllato'"
    ],
    "'Lana di roccia agricola'": [
        "'Ambiente secco controllato'"
    ],
    "'Compost sterile'": [
        "'Conservazione biomasse organiche'",
        "'Ambiente fresco controllato'"
    ],
    "'Biofertilizzante microbico'": [
        "'Conservazione soluzioni agricole'",
        "'Ambiente fresco controllato'"
    ],

    # MANGIMI E MATERIALI ZOOTECNICI
    "'Fieno essiccato'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Paglia'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime bovini crescita'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime bovini lattazione'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime ovicaprini'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime suini'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime pollame ovaiole'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime pollame ingrasso'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Mangime conigli'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],
    "'Sale minerale zootecnico'": [
        "'Conservazione mangimi secchi'",
        "'Ambiente secco controllato'"
    ],

    # FARMACI E PRODOTTI SANITARI
    "'Antibiotico veterinario bovini'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antibiotico veterinario suini'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antibiotico veterinario pollame'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antiparassitario bovini'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antiparassitario ovicaprini'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antiparassitario suini'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antiparassitario pollame'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Antinfiammatorio veterinario'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Disinfettante ferite animali'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Integratore vitaminico veterinario'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Reidratante orale veterinario'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],
    "'Probiotico veterinario'": [
        "'Catena del freddo sanitaria'",
        "'Refrigerazione standard'"
    ],
    "'Pomata cicatrizzante veterinaria'": [
        "'Catena del freddo sanitaria'",
        "'Ambiente fresco controllato'"
    ],

    # VACCINI
    "'Vaccino bovini respiratorio'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino bovini clostridiosi'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino bovini mastite'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino ovicaprini clostridiosi'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino ovicaprini enterotossiemia'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino suini parvovirosi'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino suini mal rosso'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino pollame Newcastle'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino pollame bronchite infettiva'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino pollame coccidiosi'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino conigli mixomatosi'": [
        "'Catena del freddo sanitaria'"
    ],
    "'Vaccino conigli malattia emorragica'": [
        "'Catena del freddo sanitaria'"
    ],

    # SOTTOPRODOTTI
    "'Lana ovina'": [
        "'Ambiente secco controllato'"
    ],
    "'Pelle bovina'": [
        "'Ambiente secco controllato'"
    ],
    "'Letame bovino'": [
        "'Conservazione biomasse organiche'"
    ],
    "'Letame ovino'": [
        "'Conservazione biomasse organiche'"
    ],
    "'Letame suino'": [
        "'Conservazione biomasse organiche'"
    ],
    "'Pollina'": [
        "'Conservazione biomasse organiche'"
    ],
    "'Piume di pollame'": [
        "'Ambiente secco controllato'"
    ],

    # ACQUA
    "'Acqua potabile'": [
        "'Ambiente fresco controllato'",
        "'Conservazione soluzioni agricole'"
    ]
}

NOME_CONSERVAZIONE = []
NOME_PRODOTTO = []

for prodotto, conservazioni in CONSERVAZIONE_PRODOTTO.items():
    for conservazione in conservazioni:
        NOME_PRODOTTO.append(prodotto)
        NOME_CONSERVAZIONE.append(conservazione)


theList=list(zip(NOME_CONSERVAZIONE, NOME_PRODOTTO))

keys = ["NOME_CONSERVAZIONE", "NOME_PRODOTTO"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_CONSERVAZIONE, NOME_PRODOTTO\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_PREVEDE_MOD_CONS", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/8_prodotto_prevede_mod_cons.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/8_prodotto_prevede_mod_cons.sql", lines)