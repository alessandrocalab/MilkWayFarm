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


#PRESCRIZIONE_ANIMALE:NOME_FARMACO ETICHETTA_ANIMALE DATA_VISITA NOME_PRODOTTO UNITA_MISURA DURATA_GIORNI QUANTITA_GIORNALIERA 

NOME_FARMACO = [
    "'Terapia respiratoria bovina 2025'",
    "'Terapia enterica bovina 2023'",
    "'Terapia caprina preventiva 2025'",
    "'Terapia clostridi caprina 2025'",
    "'Terapia ovina respiratoria 2024'",
    "'Terapia coniglio enterite 2025'",
    "'Terapia avicola biosicurezza 2025'",
    "'Terapia quaglia osservazione 2025'",
    "'Terapia anatra biosicurezza 2025'",
    "'Terapia suino respiratoria 2024'",
    "'Terapia trota acquacoltura 2025'",
    "'Terapia tilapia acquacoltura 2025'",
    "'Terapia tacchino routine 2024'",
    "'Terapia oca routine 2024'"
]

ETICHETTA_ANIMALE = [
    "'10000003'",  # Bovino nano
    "'10000003'",  # Bovino nano
    "'10000006'",  # Capra nana
    "'10000006'",  # Capra nana
    "'10000009'",  # Pecora compatta
    "'10000012'",  # Coniglio europeo
    "'10000015'",  # Gallina ovaiola
    "'10000018'",  # Quaglia giapponese
    "'10000021'",  # Anatra domestica
    "'10000024'",  # Maiale nano
    "'10000025'",  # Trota iridea
    "'10000027'",  # Tilapia nilotica
    "'10000029'",  # Tacchino nano
    "'10000030'"   # Oca domestica
]

DATA_VISITA = [
    "DATE '2024-02-10'",
    "DATE '2024-02-10'",
    "DATE '2025-01-12'",
    "DATE '2025-01-12'",
    "DATE '2025-02-18'",
    "DATE '2025-04-10'",
    "DATE '2025-07-01'",
    "DATE '2025-10-22'",
    "DATE '2025-09-18'",
    "DATE '2025-01-25'",
    "DATE '2025-02-15'",
    "DATE '2025-11-03'",
    "DATE '2024-09-10'",
    "DATE '2024-09-15'"
]

NOME_PRODOTTO = [
    "'Antibiotico veterinario base'",
    "'Integratore minerale per animali'",
    "'Antibiotico veterinario base'",
    "'Antiparassitario veterinario'",
    "'Antibiotico veterinario base'",
    "'Antibiotico veterinario base'",
    "'Disinfettante per stalla'",
    "'Integratore minerale per animali'",
    "'Disinfettante per stalla'",
    "'Antibiotico veterinario base'",
    "'Antibiotico veterinario base'",
    "'Antibiotico veterinario base'",
    "'Antiparassitario veterinario'",
    "'Integratore minerale per animali'"
]

UNITA_MISURA = [
    "'ml'",
    "'kg'",
    "'ml'",
    "'ml'",
    "'ml'",
    "'ml'",
    "'l'",
    "'kg'",
    "'l'",
    "'ml'",
    "'ml'",
    "'ml'",
    "'ml'",
    "'kg'"
]

DURATA_GIORNI = [
    5,
    10,
    4,
    3,
    5,
    4,
    2,
    7,
    2,
    6,
    5,
    5,
    3,
    8
]

QUANTITA_GIORNALIERA = [
    12.00,  # ml/giorno antibiotico bovino
    0.15,   # kg/giorno integratore bovino
    5.00,   # ml/giorno antibiotico capra
    3.00,   # ml/giorno antiparassitario capra
    5.00,   # ml/giorno antibiotico pecora
    1.50,   # ml/giorno antibiotico coniglio
    0.30,   # l/giorno disinfettante area avicola
    0.02,   # kg/giorno integratore quaglia
    0.25,   # l/giorno disinfettante area anatra
    8.00,   # ml/giorno antibiotico maiale
    0.50,   # ml/giorno antibiotico trota
    0.50,   # ml/giorno antibiotico tilapia
    2.00,   # ml/giorno antiparassitario tacchino
    0.05    # kg/giorno integratore oca
]


theList=list(zip(NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA))

keys = ["NOME_FARMACO", "ETICHETTA_ANIMALE", "DATA_VISITA", "NOME_PRODOTTO", "UNITA_MISURA", "DURATA_GIORNI", "QUANTITA_GIORNALIERA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_FARMACO, ETICHETTA_ANIMALE, DATA_VISITA, NOME_PRODOTTO, UNITA_MISURA, DURATA_GIORNI, QUANTITA_GIORNALIERA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRESCRIZIONE_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/8_prescrizione_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/8_prescrizione_animale.sql", lines)