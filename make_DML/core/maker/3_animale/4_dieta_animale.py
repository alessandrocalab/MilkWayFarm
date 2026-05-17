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


#DIETA_ANIMALE:NOME_DIETA OBIETTIVO_DIETA 
NOME_DIETA = [
    # Bovino nano
    "'Dieta vitello bovino nano'",
    "'Dieta giovane bovino nano'",
    "'Dieta adulto bovino nano'",

    # Capra nana
    "'Dieta capretto capra nana'",
    "'Dieta giovane capra nana'",
    "'Dieta adulto capra nana'",

    # Pecora compatta
    "'Dieta agnello pecora compatta'",
    "'Dieta giovane pecora compatta'",
    "'Dieta adulto pecora compatta'",

    # Coniglio europeo
    "'Dieta cucciolo coniglio europeo'",
    "'Dieta giovane coniglio europeo'",
    "'Dieta adulto coniglio europeo'",

    # Gallina ovaiola
    "'Dieta pulcino gallina ovaiola'",
    "'Dieta pollastra gallina ovaiola'",
    "'Dieta adulto gallina ovaiola'",

    # Quaglia giapponese
    "'Dieta pulcino quaglia giapponese'",
    "'Dieta giovane quaglia giapponese'",
    "'Dieta adulto quaglia giapponese'",

    # Anatra domestica
    "'Dieta anatroccolo anatra domestica'",
    "'Dieta giovane anatra domestica'",
    "'Dieta adulto anatra domestica'",

    # Maiale nano
    "'Dieta suinetto maiale nano'",
    "'Dieta giovane maiale nano'",
    "'Dieta adulto maiale nano'",

    # Trota iridea
    "'Dieta avannotto trota iridea'",
    "'Dieta giovane trota iridea'",
    "'Dieta adulto trota iridea'",

    # Tilapia nilotica
    "'Dieta avannotto tilapia nilotica'",
    "'Dieta giovane tilapia nilotica'",
    "'Dieta adulto tilapia nilotica'",

    # Tacchino nano
    "'Dieta pulcino tacchino nano'",
    "'Dieta giovane tacchino nano'",
    "'Dieta adulto tacchino nano'",

    # Oca domestica
    "'Dieta papero oca domestica'",
    "'Dieta giovane oca domestica'",
    "'Dieta adulto oca domestica'"
]

OBIETTIVO_DIETA = [
    # Bovino nano
    "'CRESCITA'",
    "'CRESCITA'",
    "'MANTENIMENTO'",

    # Capra nana
    "'CRESCITA'",
    "'CRESCITA'",
    "'MANTENIMENTO'",

    # Pecora compatta
    "'CRESCITA'",
    "'CRESCITA'",
    "'MANTENIMENTO'",

    # Coniglio europeo
    "'CRESCITA'",
    "'CRESCITA'",
    "'MANTENIMENTO'",

    # Gallina ovaiola
    "'CRESCITA'",
    "'CRESCITA'",
    "'RIPRODUZIONE'",

    # Quaglia giapponese
    "'CRESCITA'",
    "'CRESCITA'",
    "'RIPRODUZIONE'",

    # Anatra domestica
    "'CRESCITA'",
    "'CRESCITA'",
    "'RIPRODUZIONE'",

    # Maiale nano
    "'CRESCITA'",
    "'INGRASSO'",
    "'MANTENIMENTO'",

    # Trota iridea
    "'CRESCITA'",
    "'INGRASSO'",
    "'MANTENIMENTO'",

    # Tilapia nilotica
    "'CRESCITA'",
    "'INGRASSO'",
    "'MANTENIMENTO'",

    # Tacchino nano
    "'CRESCITA'",
    "'INGRASSO'",
    "'MANTENIMENTO'",

    # Oca domestica
    "'CRESCITA'",
    "'INGRASSO'",
    "'MANTENIMENTO'"
]


theList=list(zip(NOME_DIETA, OBIETTIVO_DIETA))

keys = ["NOME_DIETA", "OBIETTIVO_DIETA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_DIETA, OBIETTIVO_DIETA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DIETA_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/4_dieta_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/4_dieta_animale.sql", lines)