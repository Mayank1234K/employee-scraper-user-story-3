import logging
logging.disable(logging.CRITICAL)

import unittest
from unittest.mock import patch, mock_open
from scraper.downloader import download_zip

class TestDownloader(unittest.TestCase):

    @patch("scraper.downloader.requests.get")
    def test_successful_download(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"data"
        mock_get.return_value.raise_for_status = lambda: None

        with patch("builtins.open", mock_open()):
            result = download_zip("http://fake-url.com", "file.zip")

        self.assertTrue(result)

    @patch("scraper.downloader.requests.get")
    def test_download_failure(self, mock_get):
        import requests
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        result = download_zip("http://fake-url.com", "file.zip", retries=1)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
