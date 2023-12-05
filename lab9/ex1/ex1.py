from lab9.ex1.csv_validator.csv_validator import CSVValidator

file_path = 'C:\\Users\\Valea\\Desktop\\py\\lab9\\ex1\\csv_validator\\example_data.csv'
config_path = 'C:\\Users\\Valea\\Desktop\\py\\lab9\\ex1\\csv_validator\\validation_rules.yaml'

validator = CSVValidator(file_path, config_path)
validator.read_csv()

try:
    validator.validate_rules()
    print("CSV validation passed!")
except ValueError as e:
    print(f"Validation failed: {e}")

    if "Column 'Age' has 1 missing values." in str(e):
        default_value = 0
        validator.data['Age'].fillna(default_value, inplace=True)

        try:
            validator.validate_rules()
            print("CSV validation passed after handling missing values!")
        except ValueError as e:
            print(f"Validation still failed after handling missing values: {e}")