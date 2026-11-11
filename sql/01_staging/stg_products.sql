
CREATE OR REPLACE VIEW stg_products AS

SELECT
    p.product_id,
    p.product_category_name AS category_name_pt,
    COALESCE(
        t.product_category_name_english,
        p.product_category_name,
        'Unknown'
    ) AS category_name_en,
    p.product_name_lenght AS product_name_length,
    p.product_description_lenght AS product_description_length,
    p.product_photos_qty AS photos_count,
    p.product_weight_g AS weight_g,
    p.product_length_cm AS length_cm,
    p.product_height_cm AS height_cm,
    p.product_width_cm AS width_cm

FROM raw_olist_products_dataset p

LEFT JOIN raw_product_category_name_translation t
    ON p.product_category_name = t.product_category_name;
