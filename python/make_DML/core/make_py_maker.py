# inserire il path DDL e creerà un file python interattivo
# per costruire/appendere il corrispettivo DML

import os
import sys
from pathlib import Path
from textwrap import dedent

ROOT_NAME = "MilkWayFarm"

MAKER_BASE_PATH = Path("python/make_DML/core/maker")
DATA_PATH = Path("python/make_DML/data")
DML_PATH = Path("DB/DML")


def go_to_project_root() -> Path:
    current = Path.cwd().resolve()

    while current.name != ROOT_NAME:
        if current.parent == current:
            raise RuntimeError(f"Cartella {ROOT_NAME} non trovata risalendo dal path corrente.")
        current = current.parent

    os.chdir(current)

    if str(current) not in sys.path:
        sys.path.append(str(current))

    return current


go_to_project_root()

from python.make_DML.core.utils.get_table_data import getTableData


def numeric_prefix(path: Path) -> int:
    """
    Ordina file/cartelle tipo:
    1_tipo.sql
    2_animale.sql
    10_associazioni.sql
    """
    try:
        return int(path.name.split("_")[0])
    except ValueError:
        return 10**9


def build_generated_maker_text(
    table_name: str,
    attr_list: list[str],
    json_path: Path,
    dml_path: Path
) -> str:
    return dedent(f"""
    import os
    import sys
    import json
    import re
    from pathlib import Path

    ROOT_NAME = "MilkWayFarm"

    TABLE_NAME = {table_name!r}
    ATTRIBUTES = {attr_list!r}

    JSON_PATH = Path({json_path.as_posix()!r})
    DML_PATH = Path({dml_path.as_posix()!r})

    HEADER = "--" + ", ".join(ATTRIBUTES)


    def go_to_project_root() -> Path:
        current = Path.cwd().resolve()

        while current.name != ROOT_NAME:
            if current.parent == current:
                raise RuntimeError(f"Cartella {{ROOT_NAME}} non trovata risalendo dal path corrente.")
            current = current.parent

        os.chdir(current)

        if str(current) not in sys.path:
            sys.path.append(str(current))

        return current


    go_to_project_root()

    from python.make_DML.core.utils.make_DML_line import make_DML_line


    def is_number(raw: str) -> bool:
        \"\"\"
        Riconosce numeri veri:
        10
        10.5
        0.25

        Non considera numeri codici con zeri davanti:
        0001
        0000000001
        \"\"\"
        raw = raw.replace(",", ".")

        return re.fullmatch(r"[+-]?((0)|(0\\.\\d+)|([1-9]\\d*)(\\.\\d+)?)", raw) is not None


    def parse_value(attr: str, raw: str) -> str:
        raw = raw.strip()

        if raw == "":
            return "NULL"

        upper = raw.upper()

        if upper == "NULL":
            return "NULL"

        # se vuoi scrivere SQL puro:
        # =SYSDATE
        # =TO_DATE('2026-01-01','YYYY-MM-DD')
        if raw.startswith("="):
            return raw[1:].strip()

        # per attributi DATA puoi scrivere direttamente 2026-01-01
        if "DATA" in attr.upper() and re.fullmatch(r"\\d{{4}}-\\d{{2}}-\\d{{2}}", raw):
            return f"DATE '{{raw}}'"

        # SQL già valido
        if upper.startswith("DATE "):
            return raw

        if upper.startswith("TIMESTAMP "):
            return raw

        if upper.startswith("TO_DATE("):
            return raw

        if upper in ("SYSDATE", "CURRENT_DATE"):
            return raw

        # stringa già quotata
        if len(raw) >= 2 and raw[0] == "'" and raw[-1] == "'":
            return raw

        # numero
        if is_number(raw):
            return raw.replace(",", ".")

        # stringa normale: aggiungo apici e faccio escape
        escaped = raw.replace("'", "''")
        return f"'{{escaped}}'"


    def ask_int(prompt: str) -> int:
        while True:
            value = input(prompt).strip()

            try:
                n = int(value)
                if n < 0:
                    print("Inserisci un numero >= 0.")
                    continue
                return n
            except ValueError:
                print("Valore non valido. Inserisci un numero intero.")


    def collect_rows() -> list[tuple]:
        print()
        print(f"TABELLA: {{TABLE_NAME}}")
        print("Attributi:")
        for attr in ATTRIBUTES:
            print(f"  - {{attr}}")

        print()
        print("Regole input:")
        print("  - stringhe: puoi scriverle senza apici")
        print("  - numeri: scrivili normalmente, es. 12.5")
        print("  - NULL: lascia vuoto oppure scrivi NULL")
        print("  - date: per attributi DATA puoi scrivere 2026-01-01")
        print("  - SQL puro: metti '=' davanti, es. =SYSDATE")
        print()

        n = ask_int("Quante tuple vuoi inserire? ")

        rows = []

        for i in range(n):
            print()
            print(f"--- TUPLA {{i + 1}}/{{n}} ---")

            row = []

            for attr in ATTRIBUTES:
                raw = input(f"{{attr}}: ")
                value = parse_value(attr, raw)
                row.append(value)

            rows.append(tuple(row))

        return rows


    def load_existing_json(path: Path) -> list[dict]:
        if not path.exists() or path.stat().st_size == 0:
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"Il file JSON {{path}} non contiene una lista.")

        return data


    def append_json(rows: list[tuple]) -> None:
        JSON_PATH.parent.mkdir(parents=True, exist_ok=True)

        old_data = load_existing_json(JSON_PATH)

        new_data = [
            dict(zip(ATTRIBUTES, row))
            for row in rows
        ]

        final_data = old_data + new_data

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(final_data, f, indent=4, ensure_ascii=False)


    def remove_final_commit(sql_text: str) -> str:
        return re.sub(
            r"\\s*COMMIT;\\s*$",
            "\\n",
            sql_text,
            flags=re.IGNORECASE
        )


    def append_dml(rows: list[tuple]) -> None:
        DML_PATH.parent.mkdir(parents=True, exist_ok=True)

        file_exists = DML_PATH.exists()
        old_text = ""

        if file_exists:
            old_text = DML_PATH.read_text(encoding="utf-8")

        old_text_stripped = old_text.strip()

        if old_text_stripped:
            old_text = remove_final_commit(old_text)

        lines = old_text

        # Se il file non esiste o è vuoto, metto il commento iniziale.
        # Se esiste già, NON lo ripeto.
        if not old_text_stripped:
            lines += HEADER + "\\n"
        elif not lines.endswith("\\n"):
            lines += "\\n"

        for row in rows:
            lines += make_DML_line(TABLE_NAME, row) + "\\n"

        lines += "COMMIT;\\n"

        DML_PATH.write_text(lines, encoding="utf-8")


    def main() -> None:
        rows = collect_rows()

        if len(rows) == 0:
            print("Nessuna tupla inserita.")
            return

        append_json(rows)
        append_dml(rows)

        print()
        print(f"OK: aggiunte {{len(rows)}} tuple.")
        print(f"JSON aggiornato: {{JSON_PATH}}")
        print(f"DML aggiornato: {{DML_PATH}}")


    if __name__ == "__main__":
        main()
    """).lstrip()


def makePyMaker(path: str) -> None:
    path = Path(path)

    data = getTableData(str(path))
    table_name = data[0]
    attr_list = data[1]

    # esempio:
    # DB/DDL/3_animale/4_dieta_animale.sql
    # diventa:
    # 3_animale/4_dieta_animale.sql
    relative_sql_path = Path(path.parts[-2]) / path.parts[-1]

    relative_json_path = relative_sql_path.with_suffix(".json")
    relative_py_path = relative_sql_path.with_suffix(".py")

    json_path = DATA_PATH / relative_json_path
    dml_path = DML_PATH / relative_sql_path
    maker_path = MAKER_BASE_PATH / relative_py_path

    maker_text = build_generated_maker_text(
        table_name=table_name,
        attr_list=attr_list,
        json_path=json_path,
        dml_path=dml_path
    )

    maker_path.parent.mkdir(parents=True, exist_ok=True)

    with open(maker_path, "w", encoding="utf-8") as f:
        f.write(maker_text)

    print(f"Creato/aggiornato maker: {maker_path}")


if __name__ == "__main__":
    DDL_PATH = Path("./DB/DDL")

    ddl_dirs = [
        p for p in DDL_PATH.iterdir()
        if p.is_dir()
    ]

    ddl_dirs = sorted(ddl_dirs, key=numeric_prefix)

    for ddl_dir in ddl_dirs:
        sql_files = [
            p for p in ddl_dir.iterdir()
            if p.is_file()
            and p.suffix.lower() == ".sql"
            and p.name != "main.sql"
        ]

        sql_files = sorted(sql_files, key=numeric_prefix)

        for sql_file in sql_files:
            makePyMaker(str(sql_file))