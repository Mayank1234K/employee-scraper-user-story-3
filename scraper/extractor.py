import zipfile
import os
import logging

logger = logging.getLogger(__name__)

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

        files = os.listdir(extract_to)

        excel_files = [f for f in files if f.endswith((".xlsx", ".xls"))]

        if not excel_files:
            raise ValueError("No Excel file found in ZIP")

        return os.path.join(extract_to, excel_files[0])

    except zipfile.BadZipFile:
        logger.error("Corrupted ZIP file")
        return None

    except Exception as e:
        logger.error(f"Extraction error: {e}")
        return None
