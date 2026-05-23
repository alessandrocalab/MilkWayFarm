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


#SERB_RISPETTA_MOD_CONS:NUMERO_SERBATOIO CODICE_AREA NOME_STRUTTURA NOME_CONSERVAZIONE 

RIGHE_SERBATOIO_RISPETTA_CONSERVAZIONE = [
    # PRIMO MODULO - A00A
    # Area compatibile con ambiente secco controllato.
    # Serbatoi generici, utili per liquidi stabili o acqua in condizioni non refrigerate.
    ("'S001'", "'A00A'", "'Primo Modulo'", "'Ambiente secco controllato'"),
    ("'S002'", "'A00A'", "'Primo Modulo'", "'Ambiente secco controllato'"),

    # PRIMO MODULO - A00B
    ("'S001'", "'A00B'", "'Primo Modulo'", "'Ambiente secco controllato'"),
    ("'S002'", "'A00B'", "'Primo Modulo'", "'Ambiente secco controllato'"),

    # STRUTTURA STOCCAGGIO - A00C
    # 273.15 - 277.15 K, 70 - 90%
    ("'S001'", "'A00C'", "'Struttura Stoccaggio'", "'Refrigerazione standard'"),

    # STRUTTURA STOCCAGGIO - A00D
    # 253.15 - 255.15 K, 30 - 60%
    ("'S002'", "'A00D'", "'Struttura Stoccaggio'", "'Congelamento standard'"),

    # STRUTTURA STOCCAGGIO - A00E
    # 275.15 - 281.15 K, 35 - 65%
    ("'S003'", "'A00E'", "'Struttura Stoccaggio'", "'Catena del freddo sanitaria'"),

    # STRUTTURA STOCCAGGIO - A00K
    # 278.15 - 298.15 K, 30 - 70%
    ("'S004'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'S005'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),

    # STRUTTURA STOCCAGGIO - A00L
    # 278.15 - 298.15 K, 30 - 60%
    ("'S006'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'S006'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),

    ("'S007'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'S007'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),

    ("'S008'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'S008'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'")
]

NUMERO_SERBATOIO = [riga[0] for riga in RIGHE_SERBATOIO_RISPETTA_CONSERVAZIONE]

CODICE_AREA = [riga[1] for riga in RIGHE_SERBATOIO_RISPETTA_CONSERVAZIONE]

NOME_STRUTTURA = [riga[2] for riga in RIGHE_SERBATOIO_RISPETTA_CONSERVAZIONE]

NOME_CONSERVAZIONE = [riga[3] for riga in RIGHE_SERBATOIO_RISPETTA_CONSERVAZIONE]
theList=list(zip(NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE))

keys = ["NUMERO_SERBATOIO", "CODICE_AREA", "NOME_STRUTTURA", "NOME_CONSERVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("SERB_RISPETTA_MOD_CONS", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/14_serb_rispetta_mod_cons.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/14_serb_rispetta_mod_cons.sql", lines)