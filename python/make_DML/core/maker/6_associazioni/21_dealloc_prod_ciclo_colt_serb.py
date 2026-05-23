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


#DEALLOC_PROD_CICLO_COLT_SERB:DATE_MIN NOME_PRODOTTO NUMERO_SERB CODICE_AREA_SERB NOME_STRUTTURA_SERB DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA QUANTITA_DEALLOCATA 

RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE = [
    # 1) GRANO DURO - Idro cereali base
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 194.40),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 17.28),

    # 2) POMODORO - Idro pomodoro standard
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-03-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 151.20),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-03-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 12.96),

    # 3) MAIS - Idro cereali base
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-06-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 129.60),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-06-01'", "'000A'", "'A00A'", "'Struttura Agricola'", 11.52),

    # 4) MAIS - Idro cereali base
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-05'", "'000B'", "'A00A'", "'Struttura Agricola'", 129.60),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-05'", "'000B'", "'A00A'", "'Struttura Agricola'", 11.52),

    # 5) SOIA - Idro soia nutriente
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-01-15'", "'000B'", "'A00A'", "'Struttura Agricola'", 172.80),
    ("DATE '2024-06-25'", "'Soluzione nutritiva concentrata'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-01-15'", "'000B'", "'A00A'", "'Struttura Agricola'", 14.40),

    # 6) LATTUGA - Idro lattuga rapida
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-01-10'", "'000B'", "'A00A'", "'Struttura Agricola'", 37.80),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-01-10'", "'000B'", "'A00A'", "'Struttura Agricola'", 3.24),

    # 7) POMODORO - Idro pomodoro intensivo
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-08-01'", "'000C'", "'A00B'", "'Struttura Agricola'", 183.60),
    ("DATE '2024-06-25'", "'Soluzione nutritiva concentrata'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-08-01'", "'000C'", "'A00B'", "'Struttura Agricola'", 16.20),

    # 8) FAGIOLO - Idro legumi base
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-04-01'", "'000C'", "'A00B'", "'Struttura Agricola'", 118.80),
    ("DATE '2024-01-02'", "'Biofertilizzante microbico'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-04-01'", "'000C'", "'A00B'", "'Struttura Agricola'", 9.72),

    # 9) PATATA - Idro tuberi substrato
    ("DATE '2023-05-25'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-10'", "'000D'", "'A00C'", "'Struttura Agricola'", 132.00),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2023-07-10'", "'000D'", "'A00C'", "'Struttura Agricola'", 10.80),

    # 10) CAROTA - Idro radici substrato
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-02-01'", "'000D'", "'A00C'", "'Struttura Agricola'", 76.80),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2024-02-01'", "'000D'", "'A00C'", "'Struttura Agricola'", 6.72),

    # 11) ZUCCHINA - Idro cucurbitacee
    ("DATE '2023-08-12'", "'Acqua potabile'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-05-10'", "'000D'", "'A00C'", "'Struttura Agricola'", 99.00),
    ("DATE '2024-06-25'", "'Soluzione nutritiva concentrata'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2025-05-10'", "'000D'", "'A00C'", "'Struttura Agricola'", 8.58),

    # 12) LATTUGA - Idro lattuga rapida
    ("DATE '2026-03-08'", "'Acqua potabile'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001A'", "'A00A'", "'Struttura Agricola II'", 37.80),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001A'", "'A00A'", "'Struttura Agricola II'", 3.24),

    # 13) FAGIOLO - Idro legumi base
    ("DATE '2026-03-08'", "'Acqua potabile'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-05-21'", "'001A'", "'A00A'", "'Struttura Agricola II'", 118.80),
    ("DATE '2024-01-02'", "'Biofertilizzante microbico'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-05-21'", "'001A'", "'A00A'", "'Struttura Agricola II'", 9.72),

    # 14) MAIS - Idro cereali base
    ("DATE '2026-03-08'", "'Acqua potabile'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001B'", "'A00A'", "'Struttura Agricola II'", 129.60),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-05'", "'001B'", "'A00A'", "'Struttura Agricola II'", 11.52),

    # 15) PATATA - Idro tuberi substrato
    ("DATE '2026-03-08'", "'Acqua potabile'", "'S007'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-04'", "'001C'", "'A00A'", "'Struttura Agricola II'", 132.00),
    ("DATE '2023-05-20'", "'Soluzione nutritiva idroponica base'", "'S006'", "'A00L'", "'Struttura Stoccaggio'", "DATE '2026-04-04'", "'001C'", "'A00A'", "'Struttura Agricola II'", 10.80)
]

DATE_MIN = [riga[0] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

NOME_PRODOTTO = [riga[1] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

NUMERO_SERB = [riga[2] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

CODICE_AREA_SERB = [riga[3] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

NOME_STRUTTURA_SERB = [riga[4] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

DATA_INIZIO = [riga[5] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

CODICE_CELLA_IDR = [riga[6] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

CODICE_AREA_CELLA = [riga[7] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

NOME_STRUTTURA_CELLA = [riga[8] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]

QUANTITA_DEALLOCATA = [riga[9] for riga in RIGHE_DEALLOC_SERBATOIO_CICLO_COLTIVAZIONE]
theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SERB", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "DATA_INIZIO", "CODICE_CELLA_IDR", "CODICE_AREA_CELLA", "NOME_STRUTTURA_CELLA", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_CICLO_COLT_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/21_dealloc_prod_ciclo_colt_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/21_dealloc_prod_ciclo_colt_serb.sql", lines)