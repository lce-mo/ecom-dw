CREATE OR REPLACE TABLE ods.ods_orders as
SELECT
    *,
    current_timestamp as etl_time
FROM
    read_csv('data/raw/orders.csv',header = true,all_varchar = true);
