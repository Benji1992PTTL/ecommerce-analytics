
WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders

    FROM stg_orders o

    INNER JOIN stg_customers c
        ON o.customer_id = c.customer_id

    GROUP BY c.customer_unique_id
)

SELECT
    COUNT(*) AS total_customers,

    COUNT(*) FILTER (
        WHERE total_orders > 1
    ) AS repeat_customers,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE total_orders > 1
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS repeat_purchase_rate_pct

FROM customer_orders;
