import pandas as pd
import yaml

class CSVValidator:
    def __init__(self, file_path, config_path):
        self.file_path = file_path
        self.config = self.load_config(config_path)
        self.data = None

    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def load_config(self, config_path):
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config

    def validate_rules(self):
        if self.data.empty:
            raise ValueError("CSV data is empty. Call read_csv() first.")

        for column, rules in self.config.items():
            if rules.get("check_missing"):
                missing_values = self.data[column].isnull().sum()
                if missing_values > 0:
                    raise ValueError(f"Column '{column}' has {missing_values} missing values.")

            expected_data_type = rules.get("data_type")
            if expected_data_type:
                actual_data_type = self.data[column].dtype
                if actual_data_type != expected_data_type:
                    raise ValueError(
                        f"Column '{column}' has incorrect data type. Expected {expected_data_type}, got {actual_data_type}.")
