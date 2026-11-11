
WITH order_values AS (
    SELECT
        o.order_id,
        SUM(i.item_price) AS order_value,
        SUM(i.freight_value) AS freight_value

    FROM stg_orders o

    INNER JOIN stg_order_items i
        ON o.order_id = i.order_id

    WHERE o.status = 'delivered'

    GROUP BY o.order_id
)

SELECT
    COUNT(*) AS delivered_orders,

    ROUND(SUM(order_value), 2)
        AS total_product_value,

    ROUND(SUM(freight_value), 2)
        AS total_freight_value,

    ROUND(AVG(order_value), 2)
        AS average_order_value

FROM order_values;
