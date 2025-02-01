import os
from django.test import TestCase
from ..chase.chase_parser import ChaseParser


class ChaseParserTests(TestCase):
    def test_pdf_parsing(self):
        test_file = os.path.join(os.path.dirname(__file__), "test_chase.pdf")
        result = ChaseParser.parse_pdf(test_file)
        self.assertGreater(len(result), 0)
        self.assertIn("description", result[0])

    def test_csv_parsing(self):
        test_file = os.path.join(os.path.dirname(__file__), "test_chase.csv")
        result = ChaseParser.parse_csv(test_file)
        self.assertGreater(len(result), 0)
        self.assertIn("amount", result[0])
