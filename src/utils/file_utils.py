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

def get_files_in_directory(directory_path, recursive=False, extensions=None):
    """
    Retrieve a list of files in the specified directory.
    
    Args:
        directory_path (str): Path to the directory.
        recursive (bool): Whether to include files from subdirectories.
        extensions (list, optional): List of file extensions to filter by (e.g., ['.txt', '.jpg']).
                                     If None, all files are included.
    
    Returns:
        list: A list of file paths.
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")
    
    files = []
    if recursive:
        for root, _, filenames in os.walk(directory_path):
            for filename in filenames:
                if extensions is None or os.path.splitext(filename)[1] in extensions:
                    files.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(directory_path):
            full_path = os.path.join(directory_path, filename)
            if os.path.isfile(full_path):
                if extensions is None or os.path.splitext(filename)[1] in extensions:
                    files.append(full_path)
    
    return files
