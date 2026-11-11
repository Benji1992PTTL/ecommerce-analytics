CREATE OR REPLACE VIEW mart_product_sales AS

SELECT
    i.order_id,
    i.order_item_id,
    o.customer_id,
    CAST(o.purchased_at AS DATE) AS purchase_date,
    i.product_id,
    i.seller_id,

    p.category_name_pt,
    p.category_name_en,
    p.product_name_length,
    p.product_description_length,
    p.photos_count,

    o.status,
    o.purchased_at,

    c.city,
    c.state,

    i.item_price,
    i.freight_value

FROM stg_order_items i

LEFT JOIN stg_products p
    ON i.product_id = p.product_id

LEFT JOIN stg_orders o
    ON i.order_id = o.order_id

LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id;
