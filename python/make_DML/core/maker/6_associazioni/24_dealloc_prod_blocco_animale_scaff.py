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


#DEALLOC_PROD_BLOCCO_ANIMALE_SCAFF:DATE_MIN NOME_PRODOTTO NUMERO_SCAFF CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF NUMERO_BLOCCO CODICE_AREA_BLOCCO NOME_STRUTTURA_BLOCCO QUANTITA_DEALLOCATA 

RIGHE_DEALLOC_SCAFFALE_ANIMALE = [
    # BLOCCO 0001 A00B - BOVINI
    ("DATE '2023-08-05'", "'Mangime bovini crescita'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0001'", "'A00B'", "'Struttura Zootecnica'", 8.00),
    ("DATE '2026-01-01'", "'Mangime bovini lattazione'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0001'", "'A00B'", "'Struttura Zootecnica'", 10.00),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00B'", "'Struttura Zootecnica'", 42.00),
    ("DATE '2026-01-01'", "'Sale minerale zootecnico'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00B'", "'Struttura Zootecnica'", 0.26),

    # BLOCCO 0002 A00B - CAPRE + PECORE
    ("DATE '2025-09-01'", "'Mangime ovicaprini'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0002'", "'A00B'", "'Struttura Zootecnica'", 5.30),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00B'", "'Struttura Zootecnica'", 12.20),
    ("DATE '2026-01-01'", "'Sale minerale zootecnico'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00B'", "'Struttura Zootecnica'", 0.09),

    # BLOCCO 0003 A00B - MAIALI
    ("DATE '2025-09-02'", "'Mangime suini'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0003'", "'A00B'", "'Struttura Zootecnica'", 11.10),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0003'", "'A00B'", "'Struttura Zootecnica'", 2.60),
    ("DATE '2024-05-14'", "'Soia'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0003'", "'A00B'", "'Struttura Zootecnica'", 0.90),

    # BLOCCO 0004 A00B - GALLINE
    ("DATE '2023-08-07'", "'Mangime pollame ovaiole'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0004'", "'A00B'", "'Struttura Zootecnica'", 0.20),
    ("DATE '2026-01-01'", "'Mangime pollame ingrasso'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0004'", "'A00B'", "'Struttura Zootecnica'", 0.42),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0004'", "'A00B'", "'Struttura Zootecnica'", 0.12),

    # BLOCCO 0005 A00B - TACCHINI
    ("DATE '2026-01-01'", "'Mangime pollame ingrasso'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0005'", "'A00B'", "'Struttura Zootecnica'", 0.82),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0005'", "'A00B'", "'Struttura Zootecnica'", 0.18),

    # BLOCCO 0006 A00B - CONIGLI
    ("DATE '2026-01-01'", "'Mangime conigli'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0006'", "'A00B'", "'Struttura Zootecnica'", 0.54),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0006'", "'A00B'", "'Struttura Zootecnica'", 0.96),
    ("DATE '2024-04-21'", "'Carota'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", "'0006'", "'A00B'", "'Struttura Zootecnica'", 0.12),
    ("DATE '2025-02-24'", "'Lattuga'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", "'0006'", "'A00B'", "'Struttura Zootecnica'", 0.06),

    # BLOCCO 0001 A00A - CAPRA
    ("DATE '2025-09-01'", "'Mangime ovicaprini'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0001'", "'A00A'", "'Struttura Zootecnica'", 1.00),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00A'", "'Struttura Zootecnica'", 2.50),
    ("DATE '2026-01-01'", "'Sale minerale zootecnico'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00A'", "'Struttura Zootecnica'", 0.02),

    # BLOCCO 0002 A00A - CONIGLIO
    ("DATE '2026-01-01'", "'Mangime conigli'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0002'", "'A00A'", "'Struttura Zootecnica'", 0.12),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00A'", "'Struttura Zootecnica'", 0.25),
    ("DATE '2024-04-21'", "'Carota'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", "'0002'", "'A00A'", "'Struttura Zootecnica'", 0.04),

    # BLOCCO 0001 A00C - GALLINA + PRESCRIZIONE POLLAME
    ("DATE '2026-01-01'", "'Mangime pollame ingrasso'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0001'", "'A00C'", "'Struttura Zootecnica'", 0.07),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00C'", "'Struttura Zootecnica'", 0.02),
    ("DATE '2025-02-01'", "'Antibiotico veterinario pollame'", "'0001'", "'A00E'", "'Struttura Stoccaggio'", "'0001'", "'A00C'", "'Struttura Zootecnica'", 0.50),

    # BLOCCO 0002 A00C - CONIGLIO + PECORA
    ("DATE '2026-01-01'", "'Mangime conigli'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 0.09),
    ("DATE '2025-09-01'", "'Mangime ovicaprini'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 0.90),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 2.35),
    ("DATE '2025-02-24'", "'Lattuga'", "'0001'", "'A00I'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 0.03),
    ("DATE '2026-01-01'", "'Sale minerale zootecnico'", "'0002'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00C'", "'Struttura Zootecnica'", 0.02),

    # BLOCCO 0003 A00C - MAIALE
    ("DATE '2025-09-02'", "'Mangime suini'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0003'", "'A00C'", "'Struttura Zootecnica'", 2.50),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0003'", "'A00C'", "'Struttura Zootecnica'", 0.60),
    ("DATE '2024-05-14'", "'Soia'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0003'", "'A00C'", "'Struttura Zootecnica'", 0.20),

    # BLOCCO 0001 A00D - GALLINE
    ("DATE '2023-08-07'", "'Mangime pollame ovaiole'", "'0001'", "'A00J'", "'Struttura Stoccaggio'", "'0001'", "'A00D'", "'Struttura Zootecnica'", 0.20),
    ("DATE '2023-11-02'", "'Mais'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0001'", "'A00D'", "'Struttura Zootecnica'", 0.03),

    # BLOCCO 0002 A00D - CONIGLI
    ("DATE '2026-01-01'", "'Mangime conigli'", "'0002'", "'A00J'", "'Struttura Stoccaggio'", "'0002'", "'A00D'", "'Struttura Zootecnica'", 0.24),
    ("DATE '2025-12-22'", "'Fieno essiccato'", "'0001'", "'A00A'", "'Struttura Stoccaggio'", "'0002'", "'A00D'", "'Struttura Zootecnica'", 0.50),
    ("DATE '2024-04-21'", "'Carota'", "'0001'", "'A00H'", "'Struttura Stoccaggio'", "'0002'", "'A00D'", "'Struttura Zootecnica'", 0.08)
]

DATE_MIN = [riga[0] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

NOME_PRODOTTO = [riga[1] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

NUMERO_SCAFF = [riga[2] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

CODICE_AREA_SCAFF = [riga[3] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

NOME_STRUTTURA_SCAFF = [riga[4] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

NUMERO_BLOCCO = [riga[5] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

CODICE_AREA_BLOCCO = [riga[6] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

NOME_STRUTTURA_BLOCCO = [riga[7] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

QUANTITA_DEALLOCATA = [riga[8] for riga in RIGHE_DEALLOC_SCAFFALE_ANIMALE]

theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SCAFF", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "NUMERO_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_STRUTTURA_BLOCCO", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SCAFF, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_BLOCCO_ANIMALE_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/24_dealloc_prod_blocco_animale_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/24_dealloc_prod_blocco_animale_scaff.sql", lines)