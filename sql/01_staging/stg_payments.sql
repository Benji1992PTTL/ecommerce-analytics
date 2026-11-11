
CREATE OR REPLACE VIEW stg_payments AS

SELECT
    order_id,
    payment_sequential,
    payment_type,
    CAST(payment_installments AS INTEGER)
        AS payment_installments,
    CAST(payment_value AS DECIMAL(12,2))
        AS payment_value

FROM raw_olist_order_payments_dataset;
