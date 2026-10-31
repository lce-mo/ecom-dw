CREATE OR REPLACE TABLE ods.ods_products as
SELECT
    *,
    current_timestamp as etl_time
FROM
    read_csv('data/raw/products.csv',header = true,all_varchar = true)
