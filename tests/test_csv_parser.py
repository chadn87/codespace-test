# tests/test_csv_parser.py
import unittest
from src.parsers.csv_parser import parse_csv

class TestCSVParser(unittest.TestCase):
    def test_parse_csv(self):
        # Replace 'sample.csv' with the path to a test CSV file
        result = parse_csv('sample.csv')
        self.assertIsNotNone(result)
        self.assertFalse(result.empty)

if __name__ == '__main__':
    unittest.main()
