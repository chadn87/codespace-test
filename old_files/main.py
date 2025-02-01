# src/main.py
from parsers.pdf_parser import parse_pdf
from parsers.csv_parser import parse_csv
from parsers.excel_parser import parse_excel
from utils.file_utils import get_file_type
from utils.file_utils import get_files_in_directory

def main():
    
    files = get_files_in_directory("data/raw", extensions=[".csv", ".xls", ".xlsx", ".pdf"])
    for file_path in files:
        print(f"Processing file: {file_path}")
        file_type = get_file_type(file_path)

        if file_type == "pdf":
            # data = parse_pdf(file_path)
            print("Skipping PDF parsing for now")
        elif file_type == "csv":
            data = parse_csv(file_path)
        elif file_type == "excel":
            data = parse_excel(file_path)
        else:
            raise ValueError("Unsupported file type")

        # Process the extracted data
        print(data)

if __name__ == "__main__":
    main()
