CREATE OR REPLACE VIEW mart_reviews AS

SELECT
    r.review_id,
    r.order_id,
    r.review_score,
    r.review_created_at,
    r.review_answered_at,

    o.customer_id,
    CAST(o.purchased_at AS DATE) AS purchase_date,
    o.status,
    o.purchased_at,
    o.delivered_at,
    o.estimated_delivery_at,

    c.state,
    c.city,

    CASE
        WHEN o.delivered_at IS NOT NULL
         AND o.estimated_delivery_at IS NOT NULL
         AND o.delivered_at > o.estimated_delivery_at
        THEN 1
        WHEN o.delivered_at IS NOT NULL
         AND o.estimated_delivery_at IS NOT NULL
        THEN 0
        ELSE NULL
    END AS is_late_delivery

FROM stg_reviews r

LEFT JOIN stg_orders o
    ON r.order_id = o.order_id

LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id;
