# src/utils/file_utils.py
import os

def get_file_type(file_path):
    """
    Determines the file type based on the file extension.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File type ('pdf', 'csv', 'excel', or 'unknown').
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext == '.pdf':
        return 'pdf'
    elif ext == '.csv':
        return 'csv'
    elif ext in ['.xls', '.xlsx']:
        return 'excel'
    else:
        return 'unknown'
