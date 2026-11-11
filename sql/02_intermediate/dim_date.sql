
CREATE OR REPLACE VIEW dim_date AS
WITH date_range AS (
    SELECT
        CAST(date_day AS DATE) AS full_date
    FROM generate_series(
        DATE '2016-01-01',
        DATE '2019-12-31',
        INTERVAL 1 DAY
    ) AS t(date_day)
)
SELECT
    full_date,
    CAST(STRFTIME(full_date, '%Y%m%d') AS INTEGER)
        AS date_key,
    YEAR(full_date) AS year,
    QUARTER(full_date) AS quarter,
    MONTH(full_date) AS month_number,
    STRFTIME(full_date, '%B') AS month_name,
    STRFTIME(full_date, '%Y-%m') AS year_month,
    WEEK(full_date) AS week_number,
    DAY(full_date) AS day_of_month,
    DAYOFWEEK(full_date) AS day_of_week
FROM date_range;
