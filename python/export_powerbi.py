
from pathlib import Path
import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "ecommerce.duckdb"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed" / "powerbi"


MARTS = [
    "mart_order_sales",
    "mart_product_sales",
    "mart_payments",
    "mart_reviews",
    "mart_deliveries",
    "dim_products",
    "dim_customers",
    "dim_sellers",
]

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(str(DB_PATH), read_only=True)

    try:
        for mart in MARTS:
            output_path = OUTPUT_DIR / f"{mart}.csv"

            con.execute(
                f"COPY (SELECT * FROM {mart}) "
                "TO ? (HEADER, DELIMITER ',')",
                [str(output_path)]
            )

            print(f"Exportado: {output_path.name}")

    finally:
        con.close()


if __name__ == "__main__":
    main()