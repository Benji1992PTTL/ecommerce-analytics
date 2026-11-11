
CREATE OR REPLACE VIEW stg_order_items AS

SELECT
    order_id,
    order_item_id,
    product_id,
    seller_id,

    CAST(shipping_limit_date AS TIMESTAMP)
        AS shipping_deadline_at,

    CAST(price AS DECIMAL(12, 2))
        AS item_price,

    CAST(freight_value AS DECIMAL(12, 2))
        AS freight_value

FROM raw_olist_order_items_dataset;
