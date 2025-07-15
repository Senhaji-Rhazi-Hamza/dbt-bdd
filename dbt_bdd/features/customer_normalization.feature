Feature: Customer normalization

  Scenario: Normalize full name into first and last names
    Given the input file is "data/input_customer_data.csv"
    And the expected file is "data/expected_normalized_customers.csv"
    When I run the transformations specified in dbt_bdd/models/transforms/
    And I run the tests specified in dbt_bdd/models/tests/
    Then the tests should pass with no diff rows