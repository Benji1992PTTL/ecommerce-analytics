
SELECT
    YEAR(purchased_at) AS sales_year,

    COUNT(*) AS delivered_orders,

    ROUND(SUM(product_value), 2)
        AS product_value,

    ROUND(AVG(product_value), 2)
        AS average_order_value

FROM mart_order_sales

WHERE status = 'delivered'
  AND item_count > 0
  AND MONTH(purchased_at) BETWEEN 1 AND 8
  AND YEAR(purchased_at) IN (2017, 2018)

GROUP BY 1
ORDER BY 1;
