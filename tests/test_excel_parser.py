# tests/test_excel_parser.py
import unittest
from src.parsers.excel_parser import parse_excel

class TestExcelParser(unittest.TestCase):
    def test_parse_excel(self):
        # Replace 'sample.xlsx' with the path to a test Excel file
        result = parse_excel('sample.xlsx')
        self.assertIsNotNone(result)
        self.assertFalse(result.empty)

if __name__ == '__main__':
    unittest.main()
