
run_transforms: 
	cd dbt_bdd && export DBT_PROFILES_DIR=.dbt && uv run dbt run --select tag:source  --select tag:transform 

display_transforms_results:
	uv run python -c "import duckdb; conn = duckdb.connect('dbt_bdd/data/dbt_bdd.duckdb'); conn.sql('select * from normalized_customers').show()"

run_bdd_tests:
	cd dbt_bdd &&  export DBT_PROFILES_DIR=.dbt && uv run behave
