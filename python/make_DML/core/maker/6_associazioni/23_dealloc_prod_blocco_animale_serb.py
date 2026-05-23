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


#DEALLOC_PROD_BLOCCO_ANIMALE_SERB:DATE_MIN NOME_PRODOTTO NUMERO_SERB CODICE_AREA_SERB NOME_STRUTTURA_SERB NUMERO_BLOCCO CODICE_AREA_BLOCCO NOME_STRUTTURA_BLOCCO QUANTITA_DEALLOCATA 

RIGHE_DEALLOC_SERBATOIO_ANIMALE = [
    # BLOCCO 0001 A00B - Bovini
    # 2 bovini adulti + 2 bovini giovani
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0001'", "'A00B'", "'Struttura Zootecnica'", 130.00),

    # BLOCCO 0002 A00B - Capre + Pecore
    # capre adulte/giovane + pecore adulte/giovane
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0002'", "'A00B'", "'Struttura Zootecnica'", 29.50),

    # BLOCCO 0003 A00B - Maiali
    # adulti + accrescimento
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0003'", "'A00B'", "'Struttura Zootecnica'", 28.00),

    # BLOCCO 0004 A00B - Galline
    # galline adulte + giovani
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0004'", "'A00B'", "'Struttura Zootecnica'", 3.00),

    # BLOCCO 0005 A00B - Tacchini
    # tacchini adulti + giovani
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0005'", "'A00B'", "'Struttura Zootecnica'", 4.00),

    # BLOCCO 0006 A00B - Conigli
    # conigli adulti + giovani/svezzamento
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0006'", "'A00B'", "'Struttura Zootecnica'", 2.60),

    # BLOCCO 0001 A00A - Capra
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0001'", "'A00A'", "'Struttura Zootecnica'", 6.00),

    # BLOCCO 0002 A00A - Coniglio
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0002'", "'A00A'", "'Struttura Zootecnica'", 0.70),

    # BLOCCO 0001 A00C - Gallina in area biosicurezza
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0001'", "'A00C'", "'Struttura Zootecnica'", 0.35),

    # BLOCCO 0002 A00C - Coniglio + Pecora in area biosicurezza
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 5.50),

    # BLOCCO 0003 A00C - Maiale in area biosicurezza
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0003'", "'A00C'", "'Struttura Zootecnica'", 6.00),

    # BLOCCO 0001 A00D - Galline nuove
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0001'", "'A00D'", "'Struttura Zootecnica'", 0.90),

    # BLOCCO 0002 A00D - Conigli nuovi
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "'0002'", "'A00D'", "'Struttura Zootecnica'", 1.40)
]
DATE_MIN = [riga[0] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

NOME_PRODOTTO = [riga[1] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

NUMERO_SERB = [riga[2] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

CODICE_AREA_SERB = [riga[3] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

NOME_STRUTTURA_SERB = [riga[4] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

NUMERO_BLOCCO = [riga[5] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

CODICE_AREA_BLOCCO = [riga[6] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

NOME_STRUTTURA_BLOCCO = [riga[7] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

QUANTITA_DEALLOCATA = [riga[8] for riga in RIGHE_DEALLOC_SERBATOIO_ANIMALE]

theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SERB", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "NUMERO_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_STRUTTURA_BLOCCO", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_BLOCCO_ANIMALE_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/23_dealloc_prod_blocco_animale_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/23_dealloc_prod_blocco_animale_serb.sql", lines)