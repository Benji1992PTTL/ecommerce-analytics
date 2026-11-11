
from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent



SQL_FILES = [
    "sql/01_staging/stg_orders.sql",
    "sql/01_staging/stg_customers.sql",
    "sql/01_staging/stg_order_items.sql",
    "sql/01_staging/stg_products.sql",
    "sql/01_staging/stg_payments.sql",
    "sql/01_staging/stg_reviews.sql",

    "sql/02_intermediate/dim_products.sql",
    "sql/02_intermediate/dim_customers.sql",
    "sql/02_intermediate/dim_sellers.sql",

    "sql/03_marts/mart_order_sales.sql",
    "sql/03_marts/mart_product_sales.sql",
    "sql/03_marts/mart_payments.sql",
    "sql/03_marts/mart_reviews.sql",
    "sql/03_marts/mart_deliveries.sql",
]

def run_script(script, *args):
    command = [
        sys.executable,
        str(PROJECT_ROOT / "python" / script),
        *args,
    ]

    print(f"\nA executar: {script}", flush=True)

    subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        check=True,
    )


def main():
    print("=== E-COMMERCE ANALYTICS PIPELINE ===")

    # 1. Carregar os CSV originais
    run_script("load_data.py")

    # 2. Validar os dados originais
    run_script("validate_data.py")

    # 3. Criar as views pela ordem correta
    for sql_file in SQL_FILES:
        run_script("run_sql.py", sql_file)

    # 4. Exportar os marts para Power BI
    run_script("export_powerbi.py")

    print("\nPipeline concluído com sucesso!")


if __name__ == "__main__":
    main()
