import re
import pandas as pd
from PyPDF2 import PdfReader
from datetime import datetime
from typing import List, Dict
from ..base_parser import BankParser


class ChaseParser(BankParser):
    @staticmethod
    def parse_csv(file_path: str) -> List[Dict]:
        df = pd.read_csv(file_path)
        transactions = []

        for _, row in df.iterrows():
            transactions.append(
                {
                    "date": datetime.strptime(row["Posting Date"], "%m/%d/%Y"),
                    "description": row["Description"],
                    "amount": float(row["Amount"]),
                    "type": "credit" if float(row["Amount"]) >= 0 else "debit",
                }
            )

        return transactions

    @staticmethod
    def parse_pdf(file_path: str) -> List[Dict]:
        transactions = []
        reader = PdfReader(file_path)

        # Chase PDF parsing logic
        for page in reader.pages:
            text = page.extract_text()
            lines = text.split("\n")

            # Example pattern for Chase transactions
            pattern = r"(\d{2}/\d{2}) (\d{2}/\d{2}) (.*?) (-?\d+\.\d{2})"
            matches = re.findall(pattern, text)

            for match in matches:
                trans_date = datetime.strptime(
                    f"{match[0]}/{datetime.now().year}", "%m/%d/%Y"
                )
                transactions.append(
                    {
                        "date": trans_date,
                        "description": match[2].strip(),
                        "amount": float(match[3]),
                        "type": "credit" if float(match[3]) >= 0 else "debit",
                    }
                )

        return transactions

    @staticmethod
    def identify(file_path: str) -> bool:
        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = PdfReader(f)
                text = reader.pages[0].extract_text()
                return "Chase" in text
        elif file_path.endswith(".csv"):
            with open(file_path, "r") as f:
                header = f.readline()
                return "Details,Posting Date,Description,Amount,Type" in header
        return False
