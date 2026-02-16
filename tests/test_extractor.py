import logging
logging.disable(logging.CRITICAL)
import unittest
from unittest.mock import patch
from scraper.extractor import extract_zip

class TestExtractor(unittest.TestCase):

    @patch("scraper.extractor.zipfile.ZipFile")
    @patch("scraper.extractor.os.listdir")
    def test_extract_success(self, mock_listdir, mock_zip):
        mock_listdir.return_value = ["employees.xlsx"]

        result = extract_zip("file.zip", "folder")

        self.assertIn("employees.xlsx", result)

if __name__ == "__main__":
    unittest.main()
