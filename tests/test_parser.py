import logging
logging.disable(logging.CRITICAL)
import unittest
from unittest.mock import patch
import pandas as pd
from scraper.parser import parse_excel

class TestParser(unittest.TestCase):

    @patch("scraper.parser.pd.read_excel")
    def test_parse_success(self, mock_read):
        df = pd.DataFrame(columns=[
            "Employee ID", "First Name", "Last Name",
            "Email", "Job Title", "Phone Number", "Hire Date"
        ])
        mock_read.return_value = df

        result = parse_excel("file.xlsx")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
