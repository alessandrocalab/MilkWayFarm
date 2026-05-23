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


#DIETA_COMPRENDE_PRODOTTO:NOME_PRODOTTO NOME_DIETA QUANTITA 

NOME_PRODOTTO = [
    # GALLINA - Pulcino
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",

    # GALLINA - Giovane
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",
    "'Mais'",

    # GALLINA - Ovodeposizione
    "'Acqua potabile'",
    "'Mangime pollame ovaiole'",
    "'Mais'",
    "'Sale minerale zootecnico'",

    # GALLINA - Adulto
    "'Acqua potabile'",
    "'Mangime pollame ovaiole'",
    "'Mais'",

    # CONIGLIO - Cucciolo
    "'Acqua potabile'",
    "'Mangime conigli'",
    "'Fieno essiccato'",

    # CONIGLIO - Svezzamento
    "'Acqua potabile'",
    "'Mangime conigli'",
    "'Fieno essiccato'",
    "'Carota'",

    # CONIGLIO - Giovane
    "'Acqua potabile'",
    "'Mangime conigli'",
    "'Fieno essiccato'",
    "'Lattuga'",

    # CONIGLIO - Adulto
    "'Acqua potabile'",
    "'Mangime conigli'",
    "'Fieno essiccato'",
    "'Carota'",

    # CAPRA - Capretto
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",

    # CAPRA - Svezzamento
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # CAPRA - Giovane
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # CAPRA - Adulto
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # PECORA - Agnello
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",

    # PECORA - Svezzamento
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # PECORA - Giovane
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # PECORA - Adulto
    "'Acqua potabile'",
    "'Mangime ovicaprini'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # MAIALE - Suinetto
    "'Acqua potabile'",
    "'Mangime suini'",
    "'Mais'",

    # MAIALE - Svezzamento
    "'Acqua potabile'",
    "'Mangime suini'",
    "'Mais'",
    "'Soia'",

    # MAIALE - Accrescimento
    "'Acqua potabile'",
    "'Mangime suini'",
    "'Mais'",
    "'Soia'",

    # MAIALE - Adulto
    "'Acqua potabile'",
    "'Mangime suini'",
    "'Mais'",
    "'Soia'",

    # BOVINO - Vitello
    "'Acqua potabile'",
    "'Mangime bovini crescita'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # BOVINO - Svezzamento
    "'Acqua potabile'",
    "'Mangime bovini crescita'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # BOVINO - Giovane
    "'Acqua potabile'",
    "'Mangime bovini crescita'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # BOVINO - Adulto
    "'Acqua potabile'",
    "'Mangime bovini lattazione'",
    "'Fieno essiccato'",
    "'Sale minerale zootecnico'",

    # TACCHINO - Pulcino
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",

    # TACCHINO - Giovane
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",
    "'Mais'",

    # TACCHINO - Ingrasso
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",
    "'Mais'",

    # TACCHINO - Adulto
    "'Acqua potabile'",
    "'Mangime pollame ingrasso'",
    "'Mais'"
]

NOME_DIETA = [
    # GALLINA
    "'Dieta Gallina Pulcino'",
    "'Dieta Gallina Pulcino'",

    "'Dieta Gallina Giovane'",
    "'Dieta Gallina Giovane'",
    "'Dieta Gallina Giovane'",

    "'Dieta Gallina Uova'",
    "'Dieta Gallina Uova'",
    "'Dieta Gallina Uova'",
    "'Dieta Gallina Uova'",

    "'Dieta Gallina Adulta'",
    "'Dieta Gallina Adulta'",
    "'Dieta Gallina Adulta'",

    # CONIGLIO
    "'Dieta Coniglio Cucciolo'",
    "'Dieta Coniglio Cucciolo'",
    "'Dieta Coniglio Cucciolo'",

    "'Dieta Coniglio Svezz'",
    "'Dieta Coniglio Svezz'",
    "'Dieta Coniglio Svezz'",
    "'Dieta Coniglio Svezz'",

    "'Dieta Coniglio Giovane'",
    "'Dieta Coniglio Giovane'",
    "'Dieta Coniglio Giovane'",
    "'Dieta Coniglio Giovane'",

    "'Dieta Coniglio Adulto'",
    "'Dieta Coniglio Adulto'",
    "'Dieta Coniglio Adulto'",
    "'Dieta Coniglio Adulto'",

    # CAPRA
    "'Dieta Capra Capretto'",
    "'Dieta Capra Capretto'",
    "'Dieta Capra Capretto'",

    "'Dieta Capra Svezz'",
    "'Dieta Capra Svezz'",
    "'Dieta Capra Svezz'",
    "'Dieta Capra Svezz'",

    "'Dieta Capra Giovane'",
    "'Dieta Capra Giovane'",
    "'Dieta Capra Giovane'",
    "'Dieta Capra Giovane'",

    "'Dieta Capra Adulta'",
    "'Dieta Capra Adulta'",
    "'Dieta Capra Adulta'",
    "'Dieta Capra Adulta'",

    # PECORA
    "'Dieta Pecora Agnello'",
    "'Dieta Pecora Agnello'",
    "'Dieta Pecora Agnello'",

    "'Dieta Pecora Svezz'",
    "'Dieta Pecora Svezz'",
    "'Dieta Pecora Svezz'",
    "'Dieta Pecora Svezz'",

    "'Dieta Pecora Giovane'",
    "'Dieta Pecora Giovane'",
    "'Dieta Pecora Giovane'",
    "'Dieta Pecora Giovane'",

    "'Dieta Pecora Adulta'",
    "'Dieta Pecora Adulta'",
    "'Dieta Pecora Adulta'",
    "'Dieta Pecora Adulta'",

    # MAIALE
    "'Dieta Maiale Suinetto'",
    "'Dieta Maiale Suinetto'",
    "'Dieta Maiale Suinetto'",

    "'Dieta Maiale Svezz'",
    "'Dieta Maiale Svezz'",
    "'Dieta Maiale Svezz'",
    "'Dieta Maiale Svezz'",

    "'Dieta Maiale Ingrasso'",
    "'Dieta Maiale Ingrasso'",
    "'Dieta Maiale Ingrasso'",
    "'Dieta Maiale Ingrasso'",

    "'Dieta Maiale Adulto'",
    "'Dieta Maiale Adulto'",
    "'Dieta Maiale Adulto'",
    "'Dieta Maiale Adulto'",

    # BOVINO
    "'Dieta Bovino Vitello'",
    "'Dieta Bovino Vitello'",
    "'Dieta Bovino Vitello'",
    "'Dieta Bovino Vitello'",

    "'Dieta Bovino Svezz'",
    "'Dieta Bovino Svezz'",
    "'Dieta Bovino Svezz'",
    "'Dieta Bovino Svezz'",

    "'Dieta Bovino Giovane'",
    "'Dieta Bovino Giovane'",
    "'Dieta Bovino Giovane'",
    "'Dieta Bovino Giovane'",

    "'Dieta Bovino Adulto'",
    "'Dieta Bovino Adulto'",
    "'Dieta Bovino Adulto'",
    "'Dieta Bovino Adulto'",

    # TACCHINO
    "'Dieta Tacchino Pulcino'",
    "'Dieta Tacchino Pulcino'",

    "'Dieta Tacchino Giovane'",
    "'Dieta Tacchino Giovane'",
    "'Dieta Tacchino Giovane'",

    "'Dieta Tacchino Ingrasso'",
    "'Dieta Tacchino Ingrasso'",
    "'Dieta Tacchino Ingrasso'",

    "'Dieta Tacchino Adulto'",
    "'Dieta Tacchino Adulto'",
    "'Dieta Tacchino Adulto'"
]

QUANTITA = [
    # GALLINA - Pulcino
    0.250,
    0.035,

    # GALLINA - Giovane
    0.350,
    0.070,
    0.015,

    # GALLINA - Ovodeposizione
    0.500,
    0.120,
    0.020,
    0.002,

    # GALLINA - Adulto
    0.450,
    0.100,
    0.015,

    # CONIGLIO - Cucciolo
    0.150,
    0.030,
    0.020,

    # CONIGLIO - Svezzamento
    0.300,
    0.060,
    0.080,
    0.020,

    # CONIGLIO - Giovane
    0.500,
    0.090,
    0.150,
    0.030,

    # CONIGLIO - Adulto
    0.700,
    0.120,
    0.250,
    0.040,

    # CAPRA - Capretto
    1.500,
    0.250,
    0.300,

    # CAPRA - Svezzamento
    2.500,
    0.500,
    0.800,
    0.008,

    # CAPRA - Giovane
    4.000,
    0.800,
    1.500,
    0.012,

    # CAPRA - Adulto
    6.000,
    1.000,
    2.500,
    0.018,

    # PECORA - Agnello
    1.200,
    0.200,
    0.250,

    # PECORA - Svezzamento
    2.200,
    0.450,
    0.700,
    0.007,

    # PECORA - Giovane
    3.500,
    0.700,
    1.300,
    0.010,

    # PECORA - Adulto
    5.000,
    0.900,
    2.200,
    0.015,

    # MAIALE - Suinetto
    1.000,
    0.400,
    0.100,

    # MAIALE - Svezzamento
    2.500,
    0.900,
    0.200,
    0.080,

    # MAIALE - Accrescimento
    6.000,
    2.500,
    0.600,
    0.200,

    # MAIALE - Adulto
    5.000,
    1.800,
    0.400,
    0.150,

    # BOVINO - Vitello
    8.000,
    1.200,
    2.000,
    0.020,

    # BOVINO - Svezzamento
    15.000,
    2.500,
    5.000,
    0.035,

    # BOVINO - Giovane
    25.000,
    4.000,
    9.000,
    0.050,

    # BOVINO - Adulto
    40.000,
    5.000,
    12.000,
    0.080,

    # TACCHINO - Pulcino
    0.300,
    0.050,

    # TACCHINO - Giovane
    0.800,
    0.160,
    0.030,

    # TACCHINO - Ingrasso
    1.500,
    0.350,
    0.080,

    # TACCHINO - Adulto
    1.200,
    0.250,
    0.060
]

theList=list(zip(NOME_PRODOTTO, NOME_DIETA, QUANTITA))

keys = ["NOME_PRODOTTO", "NOME_DIETA", "QUANTITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_DIETA, QUANTITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DIETA_COMPRENDE_PRODOTTO", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/2_dieta_comprende_prodotto.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/2_dieta_comprende_prodotto.sql", lines)