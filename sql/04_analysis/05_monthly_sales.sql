
SELECT
    DATE_TRUNC('month', purchased_at)
        AS sales_month,

    COUNT(*) AS delivered_orders,

    ROUND(SUM(product_value), 2)
        AS product_value,

    ROUND(
        SUM(product_value) / NULLIF(COUNT(*), 0),
        2
    ) AS average_order_value

FROM mart_order_sales

WHERE status = 'delivered'
  AND purchased_at IS NOT NULL
  AND item_count > 0

GROUP BY 1
ORDER BY 1;
