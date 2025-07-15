import subprocess
import os
from behave import given, when, then

@given('the input file is "{input_path}"')
def step_given_input_file(ctx, input_path):
    ctx.input_file = input_path

@given('the expected file is "{expected_path}"')
def step_given_expected_file(ctx, expected_path):
    ctx.expected_file = expected_path

@when("I run the transformations specified in dbt_bdd/models/transforms/")
def step_run_transformation(ctx):
    result = subprocess.run([
        "dbt", "run",
        "--select", "tag:source", "tag:transform",
        "--vars", f'{{"input_file": "{ctx.input_file}"}}'
    ], capture_output=True, text=True, env=os.environ)

    print(result.stdout)
    assert result.returncode == 0, f"Transformation failed:\n{result.stderr}"

@when("I run the tests specified in dbt_bdd/models/tests/")
def step_run_test(ctx):
    result = subprocess.run([
        "dbt", "run",
        "--select", "tag:test",
        "--vars", f'{{"expected_file": "{ctx.expected_file}"}}'
    ], capture_output=True, text=True, env=os.environ)

    ctx.test_output = result.stdout
    ctx.test_returncode = result.returncode
    
    print(result.stdout)

@then("the tests should pass with no diff rows")
def step_check_diff_is_empty(ctx):
    import duckdb
    db_path = os.path.join(os.getcwd(), "data/dbt_bdd.duckdb")
    con = duckdb.connect(db_path)

    # Query the test model (a view)
    row_count = con.execute("SELECT COUNT(*) FROM test_normalized_customers").fetchone()[0]
    assert row_count == 0, f"{row_count} diff rows found in test_normalized_customers"

