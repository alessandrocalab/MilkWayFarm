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


#CELLA_IDR_RISPETTA_MOD_COLT:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA NOME_MOD_COLTIVAZIONE 

RIGHE_CELLA_RISPETTA_MODALITA = [
    # STRUTTURA AGRICOLA - celle vecchie/smontate

    # 000A - NFT
    ("'000A'", "'A00A'", "'Struttura Agricola'", "'Idro cereali base'"),
    ("'000A'", "'A00A'", "'Struttura Agricola'", "'Idro lattuga rapida'"),
    ("'000A'", "'A00A'", "'Struttura Agricola'", "'Idro legumi base'"),

    # 000B - DWC
    ("'000B'", "'A00A'", "'Struttura Agricola'", "'Idro lattuga rapida'"),
    ("'000B'", "'A00A'", "'Struttura Agricola'", "'Idro cereali base'"),

    # 000C - Aeroponica
    ("'000C'", "'A00B'", "'Struttura Agricola'", "'Idro pomodoro intensivo'"),
    ("'000C'", "'A00B'", "'Struttura Agricola'", "'Idro pomodoro standard'"),
    ("'000C'", "'A00B'", "'Struttura Agricola'", "'Idro cucurbitacee'"),

    # 000D - Letto a substrato
    ("'000D'", "'A00C'", "'Struttura Agricola'", "'Idro pomodoro standard'"),
    ("'000D'", "'A00C'", "'Struttura Agricola'", "'Idro cucurbitacee'"),
    ("'000D'", "'A00C'", "'Struttura Agricola'", "'Idro legumi base'"),

    # STRUTTURA AGRICOLA II - celle attive

    # 001A - NFT
    ("'001A'", "'A00A'", "'Struttura Agricola II'", "'Idro cereali base'"),
    ("'001A'", "'A00A'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),
    ("'001A'", "'A00A'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'001A'", "'A00A'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 001B - DWC
    ("'001B'", "'A00A'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),
    ("'001B'", "'A00A'", "'Struttura Agricola II'", "'Idro cereali base'"),
    ("'001B'", "'A00A'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'001B'", "'A00A'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 001C - Letto a substrato
    ("'001C'", "'A00A'", "'Struttura Agricola II'", "'Idro pomodoro standard'"),
    ("'001C'", "'A00A'", "'Struttura Agricola II'", "'Idro cucurbitacee'"),
    ("'001C'", "'A00A'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'001C'", "'A00A'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 002A - NFT
    ("'002A'", "'A00B'", "'Struttura Agricola II'", "'Idro cereali base'"),
    ("'002A'", "'A00B'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),
    ("'002A'", "'A00B'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'002A'", "'A00B'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 002B - DWC
    ("'002B'", "'A00B'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),
    ("'002B'", "'A00B'", "'Struttura Agricola II'", "'Idro cereali base'"),
    ("'002B'", "'A00B'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'002B'", "'A00B'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 002C - Aeroponica
    ("'002C'", "'A00B'", "'Struttura Agricola II'", "'Idro pomodoro intensivo'"),
    ("'002C'", "'A00B'", "'Struttura Agricola II'", "'Idro pomodoro standard'"),
    ("'002C'", "'A00B'", "'Struttura Agricola II'", "'Idro cucurbitacee'"),
    ("'002C'", "'A00B'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),

    # 002D - Letto a substrato
    ("'002D'", "'A00B'", "'Struttura Agricola II'", "'Idro pomodoro standard'"),
    ("'002D'", "'A00B'", "'Struttura Agricola II'", "'Idro cucurbitacee'"),
    ("'002D'", "'A00B'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'002D'", "'A00B'", "'Struttura Agricola II'", "'Idro soia nutriente'"),

    # 002E - Flusso e riflusso
    ("'002E'", "'A00B'", "'Struttura Agricola II'", "'Idro cereali base'"),
    ("'002E'", "'A00B'", "'Struttura Agricola II'", "'Idro lattuga rapida'"),
    ("'002E'", "'A00B'", "'Struttura Agricola II'", "'Idro legumi base'"),
    ("'002E'", "'A00B'", "'Struttura Agricola II'", "'Idro soia nutriente'"),
    ("'002E'", "'A00B'", "'Struttura Agricola II'", "'Idro cucurbitacee'")
]
CODICE_CELLA_IDR = [riga[0] for riga in RIGHE_CELLA_RISPETTA_MODALITA]

CODICE_AREA = [riga[1] for riga in RIGHE_CELLA_RISPETTA_MODALITA]

NOME_STRUTTURA = [riga[2] for riga in RIGHE_CELLA_RISPETTA_MODALITA]

NOME_MOD_COLTIVAZIONE = [riga[3] for riga in RIGHE_CELLA_RISPETTA_MODALITA]

theList=list(zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE))

keys = ["CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "NOME_MOD_COLTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("CELLA_IDR_RISPETTA_MOD_COLT", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/10_cella_idr_rispetta_mod_colt.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/10_cella_idr_rispetta_mod_colt.sql", lines)