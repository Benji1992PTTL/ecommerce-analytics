
SELECT
    o.status,
    COUNT(*) AS total_orders

FROM stg_orders o

LEFT JOIN stg_order_items i
    ON o.order_id = i.order_id

WHERE i.order_id IS NULL

GROUP BY o.status

ORDER BY total_orders DESC;
