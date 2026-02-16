import logging
import os
from scraper.downloader import download_zip
from scraper.extractor import extract_zip
from scraper.parser import parse_excel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="scraper.log"
)

URL = "https://www.thespreadsheetguru.com/wp-content/uploads/2022/12/EmployeeSampleData.zip"
ZIP_PATH = "employee.zip"
EXTRACT_FOLDER = "data"

def run():
    if download_zip(URL, ZIP_PATH):
        excel_file = extract_zip(ZIP_PATH, EXTRACT_FOLDER)

        if excel_file:
            df = parse_excel(excel_file)
            if df is not None:
                print(df.head())

if __name__ == "__main__":
    run()
