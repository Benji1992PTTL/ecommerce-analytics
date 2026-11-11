import duckdb
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "ecommerce.duckdb"

con = duckdb.connect(str(DB_PATH), read_only=True)

try:
    print("\n1. RESUMO DA TABELA")

    summary = con.execute("""
        SELECT
            COUNT(*) AS total_rows,
            COUNT(DISTINCT review_id) AS unique_review_ids,
            COUNT(*) - COUNT(DISTINCT review_id) AS excess_rows,
            COUNT(DISTINCT order_id) AS unique_orders
        FROM raw_olist_order_reviews_dataset
    """).fetchdf()

    print(summary.to_string(index=False))

    print("\n2. REVIEWS COM review_id REPETIDO")

    duplicates = con.execute("""
        SELECT
            review_id,
            COUNT(*) AS row_count,
            COUNT(DISTINCT order_id) AS distinct_orders,
            COUNT(DISTINCT review_score) AS distinct_scores
        FROM raw_olist_order_reviews_dataset
        GROUP BY review_id
        HAVING COUNT(*) > 1
        ORDER BY row_count DESC
        LIMIT 20
    """).fetchdf()

    print(duplicates.to_string(index=False))

    print("\n3. ORDERS COM MAIS DO QUE UMA REVIEW")

    multiple_reviews = con.execute("""
        SELECT
            order_id,
            COUNT(*) AS review_count,
            COUNT(DISTINCT review_id) AS distinct_review_ids
        FROM raw_olist_order_reviews_dataset
        GROUP BY order_id
        HAVING COUNT(*) > 1
        ORDER BY review_count DESC
        LIMIT 20
    """).fetchdf()

    print(multiple_reviews.to_string(index=False))
    print("\n4. DETALHE DOS REVIEW_ID REPETIDOS")

    details = con.execute("""
        SELECT *
        FROM raw_olist_order_reviews_dataset
        WHERE review_id = 'f4bb9d6dd4fb6dcc2298f0e7b17b8e1e'
        ORDER BY order_id
    """).fetchdf()

    print(details.to_string(index=False))

    print("\n5. DUPLICADOS DE REVIEW_ID + ORDER_ID")

    pair_duplicates = con.execute("""
        SELECT COUNT(*) AS duplicate_groups
        FROM (
            SELECT review_id, order_id
            FROM raw_olist_order_reviews_dataset
            GROUP BY review_id, order_id
            HAVING COUNT(*) > 1
        ) d
    """).fetchdf()

    print(pair_duplicates.to_string(index=False))

    print("\n6. LINHAS COMPLETAMENTE DUPLICADAS")

    exact_duplicates = con.execute("""
        SELECT COUNT(*) AS duplicate_groups
        FROM (
            SELECT *
            FROM raw_olist_order_reviews_dataset
            GROUP BY ALL
            HAVING COUNT(*) > 1
        ) d
    """).fetchdf()

    print(exact_duplicates.to_string(index=False))
finally:
    con.close()