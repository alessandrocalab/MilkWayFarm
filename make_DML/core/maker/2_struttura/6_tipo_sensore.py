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


#TIPO_SENSORE:NOME_PRODUTTORE NOME_MODELLO VALORE_MIN VALORE_MAX PRECISIONE GRANDEZZA_MISURATA UNITA_MISURA FREQUENZA_RILEVAMENTO_HZ 


NOME_PRODUTTORE = [
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",
    "'AgriMoon Devices'",
    "'AgriMoon Devices'",
    "'AgriMoon Devices'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'"
]

NOME_MODELLO = [
    "'LS-TEMP-100'",
    "'LS-HUM-120'",
    "'LS-PRESS-200'",

    "'ORB-CO2-310'",
    "'ORB-O2-320'",
    "'ORB-NH3-330'",

    "'BFA-BIO-TEMP-10'",
    "'BFA-BIO-HUM-20'",
    "'BFA-AIR-QUAL-30'",

    "'HSL-PH-400'",
    "'HSL-EC-410'",
    "'HSL-LIQ-TEMP-420'",

    "'ACS-LUX-500'",
    "'ACS-PAR-510'",
    "'ACS-UV-520'",

    "'ST-VIB-600'",
    "'ST-ENERGY-610'",
    "'ST-FLOW-620'",

    "'AMD-MOIST-700'",
    "'AMD-NUTRI-N-710'",
    "'AMD-NUTRI-K-720'",

    "'NHM-MASS-800'",
    "'NHM-LEVEL-810'",
    "'NHM-RAD-820'"
]

VALORE_MIN = [
    243.15,     # temperatura ambiente minima -30°C
    0,          # umidità %
    50000,      # pressione Pa

    0,          # CO2 ppm
    0,          # O2 %
    0,          # NH3 ppm

    273.15,     # temperatura biologica minima 0°C
    0,          # umidità biologica %
    0,          # qualità aria indice

    0,          # pH
    0,          # conducibilità elettrica mS/cm
    273.15,     # temperatura liquido 0°C

    0,          # lux
    0,          # PAR
    0,          # UV index

    0,          # vibrazione mm/s
    0,          # energia W
    0,          # flusso L/min

    0,          # umidità substrato %
    0,          # azoto mg/L
    0,          # potassio mg/L

    0,          # massa kg
    0,          # livello %
    0           # radiazione µSv/h
]

VALORE_MAX = [
    323.15,     # 50°C
    100,
    150000,

    10000,
    30,
    200,

    323.15,
    100,
    500,

    14,
    20,
    323.15,

    100000,
    3000,
    15,

    100,
    50000,
    500,

    100,
    500,
    500,

    5000,
    100,
    1000
]

PRECISIONE = [
    0.10,       # temperatura ±0.10 K
    1.00,       # umidità ±1%
    25.00,      # pressione ±25 Pa

    50.00,      # CO2 ±50 ppm
    0.10,       # O2 ±0.1%
    1.00,       # NH3 ±1 ppm

    0.05,       # temperatura biologica ±0.05 K
    0.50,       # umidità biologica ±0.5%
    5.00,       # qualità aria ±5 indice

    0.02,       # pH ±0.02
    0.05,       # EC ±0.05 mS/cm
    0.10,       # temperatura liquido ±0.10 K

    50.00,      # lux ±50
    5.00,       # PAR ±5
    0.10,       # UV index ±0.1

    0.10,       # vibrazione ±0.1 mm/s
    10.00,      # energia ±10 W
    0.50,       # flusso ±0.5 L/min

    1.00,       # umidità substrato ±1%
    2.00,       # azoto ±2 mg/L
    2.00,       # potassio ±2 mg/L

    0.50,       # massa ±0.5 kg
    0.50,       # livello ±0.5%
    0.01        # radiazione ±0.01 µSv/h
]

GRANDEZZA_MISURATA = [
    "'TEMPERATURA_AMBIENTE'",
    "'UMIDITA_RELATIVA'",
    "'PRESSIONE_ATMOSFERICA'",

    "'CONCENTRAZIONE_CO2'",
    "'CONCENTRAZIONE_O2'",
    "'CONCENTRAZIONE_NH3'",

    "'TEMPERATURA_BIOLOGICA'",
    "'UMIDITA_BIOLOGICA'",
    "'QUALITA_ARIA'",

    "'PH_SOLUZIONE'",
    "'CONDUCIBILITA_ELETTRICA'",
    "'TEMPERATURA_LIQUIDO'",

    "'ILLUMINAMENTO'",
    "'RADIAZIONE_PAR'",
    "'RADIAZIONE_UV'",

    "'VIBRAZIONE_STRUTTURALE'",
    "'POTENZA_ELETTRICA'",
    "'PORTATA_LIQUIDO'",

    "'UMIDITA_SUBSTRATO'",
    "'CONCENTRAZIONE_AZOTO'",
    "'CONCENTRAZIONE_POTASSIO'",

    "'MASSA_STOCCATA'",
    "'LIVELLO_RIEMPIMENTO'",
    "'RADIAZIONE_IONIZZANTE'"
]

UNITA_MISURA = [
    "'K'",
    "'%'",
    "'Pa'",

    "'ppm'",
    "'%'",
    "'ppm'",

    "'K'",
    "'%'",
    "'indice'",

    "'pH'",
    "'mS/cm'",
    "'K'",

    "'lux'",
    "'umol/m2/s'",
    "'indice'",

    "'mm/s'",
    "'W'",
    "'L/min'",

    "'%'",
    "'mg/L'",
    "'mg/L'",

    "'kg'",
    "'%'",
    "'uSv/h'"
]

FREQUENZA_RILEVAMENTO_HZ = [
    1.00,     # temperatura ambiente
    1.00,     # umidità
    1.00,     # pressione

    0.50,     # CO2
    0.50,     # O2
    0.50,     # NH3

    1.00,     # temperatura biologica
    1.00,     # umidità biologica
    0.20,     # qualità aria

    0.10,     # pH
    0.10,     # EC
    0.50,     # temperatura liquido

    1.00,     # lux
    1.00,     # PAR
    0.20,     # UV

    10.00,    # vibrazioni
    1.00,     # potenza elettrica
    1.00,     # portata liquido

    0.10,     # umidità substrato
    0.05,     # azoto
    0.05,     # potassio

    0.10,     # massa stoccata
    0.20,     # livello riempimento
    0.10      # radiazione
]

theList=list(zip(NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ))

keys = ["NOME_PRODUTTORE", "NOME_MODELLO", "VALORE_MIN", "VALORE_MAX", "PRECISIONE", "GRANDEZZA_MISURATA", "UNITA_MISURA", "FREQUENZA_RILEVAMENTO_HZ"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/6_tipo_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/6_tipo_sensore.sql", lines)