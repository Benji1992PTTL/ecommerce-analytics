from pathlib import Path
import duckdb

# Identificar as pastas do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "ecommerce.duckdb"

def main():
    # Verificar se existem ficheiros CSV
    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"Não foram encontrados CSV em {RAW_DIR}")

    # Criar a ligação à base de dados persistente
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(DB_PATH))

    try:
        print(f"Base de dados: {DB_PATH}")
        print(f"Ficheiros encontrados: {len(csv_files)}\n")

        for csv_file in csv_files:
            # Criar um nome de tabela a partir do nome do ficheiro
            table_name = f"raw_{csv_file.stem}"

            print(f"A carregar: {csv_file.name}")

            # Ler o CSV e criar/substituir a tabela
            con.execute(
                f"""
                CREATE OR REPLACE TABLE "{table_name}" AS
                SELECT *
                FROM read_csv_auto(?)
                """,
                [str(csv_file)]
            )

            # Obter o número de registos carregados
            row_count = con.execute(
                f'SELECT COUNT(*) FROM "{table_name}"'
            ).fetchone()[0]

            print(f"  Tabela: {table_name}")
            print(f"  Registos: {row_count:,}\n")

        print("Ingestão concluída com sucesso!")

    finally:
        con.close()


if __name__ == "__main__":
    main()