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


#STADIO_CRESCITA_INTOLLERANTE_SOSTANZA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE NOME_SOSTANZA 

RIGHE_STADIO_INTOLLERANTE_SOSTANZA = [
    # GALLINA
    ("'Pulcino'", "'Gallina'", "'Lectine vegetali'"),
    ("'Pulcino'", "'Gallina'", "'Raffinosio'"),
    ("'Pulcino'", "'Gallina'", "'Stachiosio'"),
    ("'Pulcino'", "'Gallina'", "'Solanina'"),
    ("'Pulcino'", "'Gallina'", "'Ossalati'"),

    ("'Giovane'", "'Gallina'", "'Solanina'"),
    ("'Giovane'", "'Gallina'", "'Lectine vegetali'"),
    ("'Giovane'", "'Gallina'", "'Raffinosio'"),

    ("'Ovodeposizione'", "'Gallina'", "'Solanina'"),
    ("'Ovodeposizione'", "'Gallina'", "'Ossalati'"),

    ("'Adulto'", "'Gallina'", "'Solanina'"),

    # CONIGLIO
    ("'Cucciolo'", "'Coniglio'", "'Lectine vegetali'"),
    ("'Cucciolo'", "'Coniglio'", "'Galatto oligosaccaridi'"),
    ("'Cucciolo'", "'Coniglio'", "'Raffinosio'"),
    ("'Cucciolo'", "'Coniglio'", "'Stachiosio'"),
    ("'Cucciolo'", "'Coniglio'", "'Solanina'"),
    ("'Cucciolo'", "'Coniglio'", "'Ossalati'"),

    ("'Svezzamento'", "'Coniglio'", "'Lattosio'"),
    ("'Svezzamento'", "'Coniglio'", "'Lectine vegetali'"),
    ("'Svezzamento'", "'Coniglio'", "'Galatto oligosaccaridi'"),
    ("'Svezzamento'", "'Coniglio'", "'Raffinosio'"),
    ("'Svezzamento'", "'Coniglio'", "'Stachiosio'"),
    ("'Svezzamento'", "'Coniglio'", "'Solanina'"),
    ("'Svezzamento'", "'Coniglio'", "'Ossalati'"),

    ("'Giovane'", "'Coniglio'", "'Lattosio'"),
    ("'Giovane'", "'Coniglio'", "'Galatto oligosaccaridi'"),
    ("'Giovane'", "'Coniglio'", "'Raffinosio'"),
    ("'Giovane'", "'Coniglio'", "'Stachiosio'"),
    ("'Giovane'", "'Coniglio'", "'Solanina'"),
    ("'Giovane'", "'Coniglio'", "'Ossalati'"),

    ("'Adulto'", "'Coniglio'", "'Lattosio'"),
    ("'Adulto'", "'Coniglio'", "'Fruttani'"),
    ("'Adulto'", "'Coniglio'", "'Solanina'"),
    ("'Adulto'", "'Coniglio'", "'Ossalati'"),

    # CAPRA
    ("'Capretto'", "'Capra'", "'Lectine vegetali'"),
    ("'Capretto'", "'Capra'", "'Raffinosio'"),
    ("'Capretto'", "'Capra'", "'Stachiosio'"),
    ("'Capretto'", "'Capra'", "'Solanina'"),

    ("'Svezzamento'", "'Capra'", "'Lectine vegetali'"),
    ("'Svezzamento'", "'Capra'", "'Raffinosio'"),
    ("'Svezzamento'", "'Capra'", "'Stachiosio'"),
    ("'Svezzamento'", "'Capra'", "'Solanina'"),
    ("'Svezzamento'", "'Capra'", "'Ossalati'"),

    ("'Giovane'", "'Capra'", "'Solanina'"),
    ("'Giovane'", "'Capra'", "'Ossalati'"),
    ("'Giovane'", "'Capra'", "'Glucosinolati'"),

    ("'Adulto'", "'Capra'", "'Solanina'"),
    ("'Adulto'", "'Capra'", "'Ossalati'"),
    ("'Adulto'", "'Capra'", "'Glucosinolati'"),

    # PECORA
    ("'Agnello'", "'Pecora'", "'Lectine vegetali'"),
    ("'Agnello'", "'Pecora'", "'Raffinosio'"),
    ("'Agnello'", "'Pecora'", "'Stachiosio'"),
    ("'Agnello'", "'Pecora'", "'Solanina'"),

    ("'Svezzamento'", "'Pecora'", "'Lectine vegetali'"),
    ("'Svezzamento'", "'Pecora'", "'Raffinosio'"),
    ("'Svezzamento'", "'Pecora'", "'Stachiosio'"),
    ("'Svezzamento'", "'Pecora'", "'Solanina'"),
    ("'Svezzamento'", "'Pecora'", "'Ossalati'"),

    ("'Giovane'", "'Pecora'", "'Solanina'"),
    ("'Giovane'", "'Pecora'", "'Ossalati'"),
    ("'Giovane'", "'Pecora'", "'Glucosinolati'"),

    ("'Adulto'", "'Pecora'", "'Solanina'"),
    ("'Adulto'", "'Pecora'", "'Ossalati'"),
    ("'Adulto'", "'Pecora'", "'Glucosinolati'"),

    # MAIALE
    ("'Suinetto'", "'Maiale'", "'Lectine vegetali'"),
    ("'Suinetto'", "'Maiale'", "'Galatto oligosaccaridi'"),
    ("'Suinetto'", "'Maiale'", "'Raffinosio'"),
    ("'Suinetto'", "'Maiale'", "'Stachiosio'"),
    ("'Suinetto'", "'Maiale'", "'Solanina'"),

    ("'Svezzamento'", "'Maiale'", "'Lectine vegetali'"),
    ("'Svezzamento'", "'Maiale'", "'Galatto oligosaccaridi'"),
    ("'Svezzamento'", "'Maiale'", "'Raffinosio'"),
    ("'Svezzamento'", "'Maiale'", "'Stachiosio'"),
    ("'Svezzamento'", "'Maiale'", "'Solanina'"),
    ("'Svezzamento'", "'Maiale'", "'Glucosinolati'"),

    ("'Accrescimento'", "'Maiale'", "'Raffinosio'"),
    ("'Accrescimento'", "'Maiale'", "'Solanina'"),
    ("'Accrescimento'", "'Maiale'", "'Glucosinolati'"),

    ("'Adulto'", "'Maiale'", "'Solanina'"),
    ("'Adulto'", "'Maiale'", "'Glucosinolati'"),

    # BOVINO
    ("'Vitello'", "'Bovino'", "'Lectine vegetali'"),
    ("'Vitello'", "'Bovino'", "'Raffinosio'"),
    ("'Vitello'", "'Bovino'", "'Stachiosio'"),
    ("'Vitello'", "'Bovino'", "'Solanina'"),

    ("'Svezzamento'", "'Bovino'", "'Lectine vegetali'"),
    ("'Svezzamento'", "'Bovino'", "'Raffinosio'"),
    ("'Svezzamento'", "'Bovino'", "'Stachiosio'"),
    ("'Svezzamento'", "'Bovino'", "'Solanina'"),
    ("'Svezzamento'", "'Bovino'", "'Ossalati'"),

    ("'Giovane'", "'Bovino'", "'Solanina'"),
    ("'Giovane'", "'Bovino'", "'Ossalati'"),
    ("'Giovane'", "'Bovino'", "'Glucosinolati'"),

    ("'Adulto'", "'Bovino'", "'Solanina'"),
    ("'Adulto'", "'Bovino'", "'Ossalati'"),
    ("'Adulto'", "'Bovino'", "'Glucosinolati'"),

    # TACCHINO
    ("'Pulcino'", "'Tacchino'", "'Lectine vegetali'"),
    ("'Pulcino'", "'Tacchino'", "'Raffinosio'"),
    ("'Pulcino'", "'Tacchino'", "'Stachiosio'"),
    ("'Pulcino'", "'Tacchino'", "'Solanina'"),
    ("'Pulcino'", "'Tacchino'", "'Ossalati'"),

    ("'Giovane'", "'Tacchino'", "'Solanina'"),
    ("'Giovane'", "'Tacchino'", "'Lectine vegetali'"),
    ("'Giovane'", "'Tacchino'", "'Raffinosio'"),

    ("'Ingrasso'", "'Tacchino'", "'Solanina'"),
    ("'Ingrasso'", "'Tacchino'", "'Lectine vegetali'"),
    ("'Ingrasso'", "'Tacchino'", "'Ossalati'"),

    ("'Adulto'", "'Tacchino'", "'Solanina'"),
    ("'Adulto'", "'Tacchino'", "'Ossalati'")
]

NOME_STADIO_CRESCITA = [riga[0] for riga in RIGHE_STADIO_INTOLLERANTE_SOSTANZA]

NOME_TIPO_ANIMALE = [riga[1] for riga in RIGHE_STADIO_INTOLLERANTE_SOSTANZA]

NOME_SOSTANZA = [riga[2] for riga in RIGHE_STADIO_INTOLLERANTE_SOSTANZA]
theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "NOME_SOSTANZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA_INTOLLERANTE_SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/4_stadio_crescita_intollerante_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/4_stadio_crescita_intollerante_sostanza.sql", lines)