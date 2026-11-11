
CREATE OR REPLACE VIEW dim_products AS
SELECT
    product_id,
    category_name_pt,
    category_name_en,
    product_name_length,
    product_description_length,
    photos_count,
    weight_g,
    length_cm,
    height_cm,
    width_cm
FROM stg_products;
