import logging
logging.disable(logging.CRITICAL)
import unittest
import pandas as pd
from scraper.validator import validate_structure

class TestValidator(unittest.TestCase):

    def test_valid_structure(self):
        df = pd.DataFrame(columns=[
            "Employee ID", "First Name", "Last Name",
            "Email", "Job Title", "Phone Number", "Hire Date"
        ])

        self.assertTrue(validate_structure(df))

    def test_missing_column(self):
        df = pd.DataFrame(columns=["Employee ID"])

        self.assertFalse(validate_structure(df))

if __name__ == "__main__":
    unittest.main()
