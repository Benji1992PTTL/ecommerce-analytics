
CREATE OR REPLACE VIEW dim_sellers AS
SELECT
    seller_id,
    seller_zip_code_prefix AS zip_code_prefix,
    seller_city AS city,
    seller_state AS state
FROM raw_olist_sellers_dataset;
