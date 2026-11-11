import duckdb
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "ecommerce.duckdb"

# Tabelas e respetivas chaves que esperamos serem únicas
KEY_CHECKS = {
    "raw_olist_customers_dataset": ["customer_id"],
    "raw_olist_orders_dataset": ["order_id"],
    "raw_olist_products_dataset": ["product_id"],
    "raw_olist_sellers_dataset": ["seller_id"],
    "raw_product_category_name_translation": ["product_category_name"],
    "raw_olist_order_items_dataset": ["order_id", "order_item_id"],
    "raw_olist_order_payments_dataset": ["order_id", "payment_sequential"],
    "raw_olist_order_reviews_dataset": ["review_id", "order_id"],
}

def main():
    con = duckdb.connect(str(DB_PATH), read_only=True)

    try:
        tables = con.execute("""
    		SELECT table_name
    		FROM information_schema.tables
    		WHERE table_schema = 'main'
      		AND table_type = 'BASE TABLE'
      		AND table_name LIKE 'raw_%'
    		ORDER BY table_name
	""").fetchall()

        table_names = {row[0] for row in tables}

        print("=" * 60)
        print("DATA QUALITY REPORT")
        print("=" * 60)

        print(f"\nTotal de tabelas encontradas: {len(table_names)}")

        if len(table_names) != 9:
            print("WARNING: Esperávamos encontrar 9 tabelas.")

        print("\n1. ROW COUNTS")

        for table in sorted(table_names):
            count = con.execute(
                f'SELECT COUNT(*) FROM "{table}"'
            ).fetchone()[0]

            print(f"{table}: {count:,} registos")

        print("\n2. PRIMARY KEY CHECKS")

        for table, columns in KEY_CHECKS.items():

            if table not in table_names:
                print(f"FAIL - Tabela em falta: {table}")
                continue

            column_list = ", ".join(
                f'"{column}"' for column in columns
            )

            null_condition = " OR ".join(
                f'"{column}" IS NULL' for column in columns
            )

            null_count = con.execute(f"""
                SELECT COUNT(*)
                FROM "{table}"
                WHERE {null_condition}
            """).fetchone()[0]

            duplicate_count = con.execute(f"""
                SELECT COUNT(*)
                FROM (
                    SELECT {column_list}
                    FROM "{table}"
                    GROUP BY {column_list}
                    HAVING COUNT(*) > 1
                ) duplicates
            """).fetchone()[0]

            status = (
                "PASS"
                if null_count == 0 and duplicate_count == 0
                else "FAIL"
            )

            print(f"\n{table}: {status}")
            print(f"  Null keys: {null_count:,}")
            print(f"  Duplicate keys: {duplicate_count:,}")

        print("\nValidation finished.")

    finally:
        con.close()


if __name__ == "__main__":
    main()