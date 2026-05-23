import os
import sys

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

import oracledb
from env.getDotEnv import get_env_required

def get_connection():
    conn=oracledb.connect(
        user=get_env_required("ORC_USER"),
        password=get_env_required("ORC_PASSWORD"),
        dsn=get_env_required("ORC_ADDRESS")
    )

    return conn
