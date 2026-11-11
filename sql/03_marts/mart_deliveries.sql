CREATE OR REPLACE VIEW mart_deliveries AS

SELECT
    o.order_id,
    o.customer_id,
    CAST(o.purchased_at AS DATE) AS purchase_date,
    o.status,
    o.purchased_at,
    o.shipped_at,
    o.delivered_at,
    o.estimated_delivery_at,

    c.state,
    c.city,

    DATE_DIFF(
        'day',
        o.purchased_at,
        o.delivered_at
    ) AS delivery_days,

    DATE_DIFF(
        'day',
        o.estimated_delivery_at,
        o.delivered_at
    ) AS days_vs_estimate,

    CASE
        WHEN o.delivered_at IS NULL
          OR o.estimated_delivery_at IS NULL
        THEN NULL

        WHEN o.delivered_at > o.estimated_delivery_at
        THEN 1

        ELSE 0
    END AS is_late_delivery

FROM stg_orders o

LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id;
