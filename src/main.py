# src/main.py
from parsers.pdf_parser import parse_pdf
from parsers.csv_parser import parse_csv
from parsers.excel_parser import parse_excel
from utils.file_utils import get_file_type

def main():
    file_path = "data/raw/20241120-statements-1983-.pdf"  # Example file path
    file_type = get_file_type(file_path)

    if file_type == "pdf":
        data = parse_pdf(file_path)
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