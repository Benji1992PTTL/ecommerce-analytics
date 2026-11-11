
from pathlib import Path
import sys
import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "ecommerce.duckdb"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python python/run_sql.py <ficheiro.sql>")

    sql_path = PROJECT_ROOT / sys.argv[1]

    if not sql_path.is_file():
        raise FileNotFoundError(sql_path)

    sql = sql_path.read_text(encoding="utf-8")

    con = duckdb.connect(str(DB_PATH))

    try:
        con.execute(sql)
        print(f"SQL executado: {sql_path.name}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
