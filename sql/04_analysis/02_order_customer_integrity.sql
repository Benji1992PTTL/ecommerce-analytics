
SELECT
    COUNT(*) AS total_orders,

    COUNT(*) FILTER (
        WHERE c.customer_id IS NULL
    ) AS orders_without_customer,

    COUNT(DISTINCT o.order_id)
        AS distinct_orders

FROM stg_orders o

LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id;
