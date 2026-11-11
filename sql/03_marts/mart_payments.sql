CREATE OR REPLACE VIEW mart_payments AS

SELECT
    p.order_id,
    p.payment_sequential,
    o.customer_id,
    CAST(o.purchased_at AS DATE) AS purchase_date,
    p.payment_type,
    p.payment_installments,
    p.payment_value,

    o.status,
    o.purchased_at

FROM stg_payments p

LEFT JOIN stg_orders o
    ON p.order_id = o.order_id;
