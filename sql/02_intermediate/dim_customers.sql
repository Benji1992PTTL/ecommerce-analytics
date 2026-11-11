
CREATE OR REPLACE VIEW dim_customers AS
SELECT
    customer_id,
    customer_unique_id,
    zip_code_prefix,
    city,
    state
FROM stg_customers;
