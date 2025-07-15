# Making Expectations Testable: DBT + BDD Boiler plate project

This project aims to show how you can use BDD pattern within DBT, BDD is not natively 
supported in BDD, and sometimes in some context it's a very important 
decision criteria to retain the solution.

So this little shows this pattern and can be used by your team as a boilerplate.


### Usage 

##### Prerequisite :
```bash 
# please this project uses uv as a package manager, it's mandatory to exec the next commands
# find how to install uv in https://docs.astral.sh/uv/getting-started/installation/

```


##### Suppose you have the following input test data 


```bash
# input data to be found in dbt_bdd/data/input_customer_data.csv
| customer_id | full_name    |
| 1           | Alice Dupond |
| 2           | Bob Durand   |
```

##### You want to test it against the expected output data


```bash
# expected output to be found in dbt_bdd/data/expected_normalized_customers.csv
| customer_id | first_name | last_name |
| 1           | Alice      | Dupond    |
| 2           | Bob        | Durand    |
```

##### Run the transformation 

```bash 
make run_transforms
```

##### Display transformation's results

```bash 
make display_transforms_results
```

##### Validate with BDD that it match the expected output

```bash 
make run_bdd_tests

# not that this is the following scenario that is checked : 
Feature: Customer normalization

  Scenario: Normalize full name into first and last names
    Given the input file is "data/input_customer_data.csv"
    And the expected file is "data/expected_normalized_customers.csv"
    When I run the transformations specified in dbt_bdd/models/transforms/
    And I run the tests specified in dbt_bdd/models/tests/
    Then the tests should pass with no diff rows

# Thes test is to be found at dbt_bdd/features/customer_normalization.feature
```