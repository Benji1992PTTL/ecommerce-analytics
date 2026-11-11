CREATE OR REPLACE VIEW mart_order_sales AS

WITH order_items_aggregated AS (
    SELECT
        order_id,
        COUNT(*) AS item_count,
        SUM(item_price) AS product_value,
        SUM(freight_value) AS freight_value

    FROM stg_order_items

    GROUP BY order_id
)

SELECT
    o.order_id,
    o.customer_id,
    CAST(o.purchased_at AS DATE) AS purchase_date,
    c.customer_unique_id,
    c.city,
    c.state,

    o.status,
    o.purchased_at,
    o.delivered_at,

    COALESCE(i.item_count, 0) AS item_count,
    COALESCE(i.product_value, 0) AS product_value,
    COALESCE(i.freight_value, 0) AS freight_value,

    COALESCE(i.product_value, 0)
        + COALESCE(i.freight_value, 0)
        AS total_order_value

FROM stg_orders o

LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id

LEFT JOIN order_items_aggregated i
    ON o.order_id = i.order_id;
