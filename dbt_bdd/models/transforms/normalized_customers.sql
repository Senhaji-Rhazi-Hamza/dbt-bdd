WITH source AS (
    SELECT * FROM {{ ref('input_customer_data') }}
)

SELECT
    customer_id,
    split_part(full_name, ' ', 1) AS first_name,
    split_part(full_name, ' ', 2) AS last_name
FROM source
