CREATE OR REPLACE TABLE ods.ods_users AS
SELECT
    *,
    current_timestamp AS etl_time
FROM read_csv('data/raw/users.csv', header = true, all_varchar = true);
