
CREATE OR REPLACE VIEW dim_orders AS
SELECT
    order_id,
    customer_id,
    status,
    purchased_at,
    CAST(purchased_at AS DATE) AS purchase_date,
    delivered_at,
    estimated_delivery_at
FROM stg_orders;
