with actual as (
  select * from {{ ref('normalized_customers') }}
),
expected as (
 select * from read_csv_auto('{{ var("expected_file", "data/expected_normalized_customers.csv") }}')
),
diff as (
  (select * from actual except select * from expected)
  union all
  (select * from expected except select * from actual)
)
select * from diff
