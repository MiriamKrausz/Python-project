import pandas as pd

class FileOperation:
    def read_csv(self, file_path: str):
        # Read data from CSV file
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return None

    def save_to_excel(self, data, file_name: str):
        # Save data to CSV file
        try:
            data.to_csv(file_name, index=False)
            print(f"Data saved to '{file_name}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving the data to CSV: {e}")


