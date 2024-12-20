# src/parsers/excel_parser.py
import pandas as pd

def parse_excel(file_path, sheet_name=0):
    """
    Reads an Excel file into a pandas DataFrame.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str or int, optional): Name or index of the sheet to read. Defaults to the first sheet (0).

    Returns:
        pd.DataFrame: DataFrame containing the Excel data.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error parsing Excel file: {e}")
        return None
