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


#SENSORE:SERIALE NOME_PRODUTTORE NOME_MODELLO CODICE_AREA NOME_STRUTTURA 

SERIALE = [
    "'SEN000001'",
    "'SEN000002'",
    "'SEN000003'",
    "'SEN000004'",
    "'SEN000005'",
    "'SEN000006'",
    "'SEN000007'",
    "'SEN000008'",
    "'SEN000009'",
    "'SEN000010'",
    "'SEN000011'",
    "'SEN000012'",
    "'SEN000013'",
    "'SEN000014'",
    "'SEN000015'",
    "'SEN000016'",
    "'SEN000017'",
    "'SEN000018'",
    "'SEN000019'",
    "'SEN000020'",
    "'SEN000021'",
    "'SEN000022'",
    "'SEN000023'",
    "'SEN000024'",
    "'SEN000025'",
    "'SEN000026'",
    "'SEN000027'",
    "'SEN000028'",
    "'SEN000029'",
    "'SEN000030'",
    "'SEN000031'",
    "'SEN000032'"
]

NOME_PRODUTTORE = [
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",

    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'BioFarm Analytics'",
    "'BioFarm Analytics'",
    "'Orbitron Instruments'",
    "'Orbitron Instruments'",

    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'AstraControl Sensors'",
    "'AstraControl Sensors'",
    "'AgriMoon Devices'",

    "'HydroSpace Lab'",
    "'HydroSpace Lab'",
    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'SeleneTech Instruments'",
    "'SeleneTech Instruments'",

    "'NovaHab Monitoring'",
    "'NovaHab Monitoring'",
    "'LunaSense Systems'",
    "'LunaSense Systems'",
    "'Orbitron Instruments'",
    "'SeleneTech Instruments'",
    "'AstraControl Sensors'",
    "'NovaHab Monitoring'"
]

NOME_MODELLO = [
    "'LS-TEMP-100'",
    "'LS-HUM-120'",
    "'LS-PRESS-200'",
    "'ORB-CO2-310'",
    "'ORB-O2-320'",
    "'ORB-NH3-330'",

    "'LS-TEMP-100'",
    "'LS-HUM-120'",
    "'BFA-BIO-TEMP-10'",
    "'BFA-BIO-HUM-20'",
    "'ORB-CO2-310'",
    "'ORB-NH3-330'",

    "'HSL-PH-400'",
    "'HSL-EC-410'",
    "'HSL-LIQ-TEMP-420'",
    "'ACS-LUX-500'",
    "'ACS-PAR-510'",
    "'AMD-MOIST-700'",

    "'HSL-PH-400'",
    "'HSL-EC-410'",
    "'NHM-LEVEL-810'",
    "'NHM-MASS-800'",
    "'ST-FLOW-620'",
    "'ST-ENERGY-610'",

    "'NHM-MASS-800'",
    "'NHM-LEVEL-810'",
    "'LS-TEMP-100'",
    "'LS-HUM-120'",
    "'ORB-O2-320'",
    "'ST-VIB-600'",
    "'ACS-UV-520'",
    "'NHM-RAD-820'"
]

CODICE_AREA = [
    "'A01A'",
    "'A01A'",
    "'A01A'",
    "'A03A'",
    "'A03A'",
    "'A03A'",

    "'A04A'",
    "'A04A'",
    "'A08A'",
    "'A08A'",
    "'A16A'",
    "'A16A'",

    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",
    "'A05A'",

    "'A06A'",
    "'A06A'",
    "'A12A'",
    "'A12A'",
    "'A12A'",
    "'A13A'",

    "'A09A'",
    "'A09A'",
    "'A10A'",
    "'A10A'",
    "'A14A'",
    "'A13A'",
    "'A15A'",
    "'A14A'"
]

NOME_STRUTTURA = [
    "'Modulo Agricolo Alfa'",
    "'Modulo Agricolo Alfa'",
    "'Modulo Agricolo Alfa'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",

    "'Modulo Zootecnico Beta'",
    "'Modulo Zootecnico Beta'",
    "'Laboratorio Biologico Delta'",
    "'Laboratorio Biologico Delta'",
    "'Modulo Quarantena Lambda'",
    "'Modulo Quarantena Lambda'",

    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",

    "'Serra Idroponica Gamma'",
    "'Serra Idroponica Gamma'",
    "'Area Serbatoi Eta'",
    "'Area Serbatoi Eta'",
    "'Area Serbatoi Eta'",
    "'Modulo Energia Theta'",

    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Deposito Alimentare Epsilon'",
    "'Centro Controllo Iota'",
    "'Modulo Energia Theta'",
    "'Cupola Osservazione Kappa'",
    "'Centro Controllo Iota'"
]


theList=list(zip(SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA))

keys = ["SERIALE", "NOME_PRODUTTORE", "NOME_MODELLO", "CODICE_AREA", "NOME_STRUTTURA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA\n"
for i in range(len(theList)):
  lines+=make_DML_line("SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/7_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/7_sensore.sql", lines)