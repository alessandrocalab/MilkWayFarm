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


#SCAFFALE_RISPETTA_MOD_CONS:NUMERO_SCAFFALE CODICE_AREA NOME_STRUTTURA NOME_CONSERVAZIONE 

RIGHE_SCAFFALE_RISPETTA_CONSERVAZIONE = [
    # PRIMO MODULO - A00A
    ("'0001'", "'A00A'", "'Primo Modulo'", "'Ambiente secco controllato'"),
    ("'0001'", "'A00A'", "'Primo Modulo'", "'Conservazione mangimi secchi'"),

    # PRIMO MODULO - A00B
    ("'0001'", "'A00B'", "'Primo Modulo'", "'Ambiente secco controllato'"),
    ("'0001'", "'A00B'", "'Primo Modulo'", "'Conservazione mangimi secchi'"),

    # STRUTTURA AGRICOLA - A00A
    ("'0001'", "'A00A'", "'Struttura Agricola'", "'Ambiente secco controllato'"),
    ("'0001'", "'A00A'", "'Struttura Agricola'", "'Conservazione mangimi secchi'"),

    # STRUTTURA STOCCAGGIO - A00A
    ("'0001'", "'A00A'", "'Struttura Stoccaggio'", "'Ambiente secco controllato'"),
    ("'0001'", "'A00A'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),
    ("'0002'", "'A00A'", "'Struttura Stoccaggio'", "'Ambiente secco controllato'"),
    ("'0002'", "'A00A'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),
    ("'0003'", "'A00A'", "'Struttura Stoccaggio'", "'Ambiente secco controllato'"),
    ("'0003'", "'A00A'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),
    ("'0004'", "'A00A'", "'Struttura Stoccaggio'", "'Ambiente secco controllato'"),
    ("'0004'", "'A00A'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),

    # STRUTTURA STOCCAGGIO - A00B
    ("'0001'", "'A00B'", "'Struttura Stoccaggio'", "'Ambiente fresco controllato'"),
    ("'0001'", "'A00B'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0002'", "'A00B'", "'Struttura Stoccaggio'", "'Ambiente fresco controllato'"),
    ("'0002'", "'A00B'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0003'", "'A00B'", "'Struttura Stoccaggio'", "'Ambiente fresco controllato'"),
    ("'0003'", "'A00B'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),

    # STRUTTURA STOCCAGGIO - A00C
    ("'0001'", "'A00C'", "'Struttura Stoccaggio'", "'Refrigerazione standard'"),
    ("'0002'", "'A00C'", "'Struttura Stoccaggio'", "'Refrigerazione standard'"),
    ("'0003'", "'A00C'", "'Struttura Stoccaggio'", "'Refrigerazione standard'"),

    # STRUTTURA STOCCAGGIO - A00D
    ("'0001'", "'A00D'", "'Struttura Stoccaggio'", "'Congelamento standard'"),
    ("'0002'", "'A00D'", "'Struttura Stoccaggio'", "'Congelamento standard'"),
    ("'0003'", "'A00D'", "'Struttura Stoccaggio'", "'Congelamento standard'"),

    # STRUTTURA STOCCAGGIO - A00E
    ("'0001'", "'A00E'", "'Struttura Stoccaggio'", "'Catena del freddo sanitaria'"),
    ("'0002'", "'A00E'", "'Struttura Stoccaggio'", "'Catena del freddo sanitaria'"),

    # STRUTTURA STOCCAGGIO - A00F
    ("'0001'", "'A00F'", "'Struttura Stoccaggio'", "'Conservazione semi breve termine'"),
    ("'0002'", "'A00F'", "'Struttura Stoccaggio'", "'Conservazione semi breve termine'"),

    # STRUTTURA STOCCAGGIO - A00G
    ("'0001'", "'A00G'", "'Struttura Stoccaggio'", "'Conservazione semi lungo termine'"),
    ("'0002'", "'A00G'", "'Struttura Stoccaggio'", "'Conservazione semi lungo termine'"),

    # STRUTTURA STOCCAGGIO - A00H
    ("'0001'", "'A00H'", "'Struttura Stoccaggio'", "'Conservazione tuberi e radici'"),
    ("'0002'", "'A00H'", "'Struttura Stoccaggio'", "'Conservazione tuberi e radici'"),
    ("'0003'", "'A00H'", "'Struttura Stoccaggio'", "'Conservazione tuberi e radici'"),

    # STRUTTURA STOCCAGGIO - A00I
    ("'0001'", "'A00I'", "'Struttura Stoccaggio'", "'Conservazione verdure fresche'"),
    ("'0002'", "'A00I'", "'Struttura Stoccaggio'", "'Conservazione verdure fresche'"),

    # STRUTTURA STOCCAGGIO - A00J
    ("'0001'", "'A00J'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),
    ("'0002'", "'A00J'", "'Struttura Stoccaggio'", "'Conservazione mangimi secchi'"),

    # STRUTTURA STOCCAGGIO - A00K
    ("'0001'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0002'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0003'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0004'", "'A00K'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),

    # STRUTTURA STOCCAGGIO - A00L
    ("'0001'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'0001'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0002'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'0002'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'"),
    ("'0003'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione soluzioni agricole'"),
    ("'0003'", "'A00L'", "'Struttura Stoccaggio'", "'Conservazione biomasse organiche'")
]
NUMERO_SCAFFALE = [riga[0] for riga in RIGHE_SCAFFALE_RISPETTA_CONSERVAZIONE]

CODICE_AREA = [riga[1] for riga in RIGHE_SCAFFALE_RISPETTA_CONSERVAZIONE]

NOME_STRUTTURA = [riga[2] for riga in RIGHE_SCAFFALE_RISPETTA_CONSERVAZIONE]

NOME_CONSERVAZIONE = [riga[3] for riga in RIGHE_SCAFFALE_RISPETTA_CONSERVAZIONE]

theList=list(zip(NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE))

keys = ["NUMERO_SCAFFALE", "CODICE_AREA", "NOME_STRUTTURA", "NOME_CONSERVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SCAFFALE, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("SCAFFALE_RISPETTA_MOD_CONS", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/13_scaffale_rispetta_mod_cons.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/13_scaffale_rispetta_mod_cons.sql", lines)