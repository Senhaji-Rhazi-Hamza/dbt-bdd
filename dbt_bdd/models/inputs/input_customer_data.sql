select * from read_csv_auto('{{ var("input_file", "data/excpected_normalized_customers.csv") }}')
