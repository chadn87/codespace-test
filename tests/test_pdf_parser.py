# tests/test_pdf_parser.py
import unittest
from src.parsers.pdf_parser import parse_pdf

class TestPDFParser(unittest.TestCase):
    def test_parse_pdf(self):
        # Replace 'sample.pdf' with the path to a test PDF file
        result = parse_pdf('sample.pdf')
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
