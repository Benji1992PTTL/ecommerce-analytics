
SELECT
    COUNT(*) AS total_items,

    COUNT(DISTINCT order_id || '-' || CAST(order_item_id AS VARCHAR))
        AS unique_order_items,

    ROUND(SUM(item_price), 2) AS total_product_value,

    ROUND(SUM(freight_value), 2) AS total_freight_value,

    COUNT(*) FILTER (
        WHERE category_name_en IS NULL
    ) AS missing_categories,

    COUNT(*) FILTER (
        WHERE status = 'delivered'
    ) AS delivered_items,

    ROUND(
        SUM(item_price) FILTER (
            WHERE status = 'delivered'
        ), 2
    ) AS delivered_product_value

FROM mart_product_sales;