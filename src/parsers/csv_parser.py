# src/parsers/csv_parser.py
import pandas as pd

def parse_csv(file_path):
    """
    Reads a CSV file into a DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return None
