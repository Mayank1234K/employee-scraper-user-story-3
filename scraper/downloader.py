import requests
import logging
import time

logger = logging.getLogger(__name__)

def download_zip(url, output_path, retries=3):
    attempt = 0

    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                f.write(response.content)

            logger.info("Download successful")
            return True

        except requests.exceptions.RequestException as e:
            attempt += 1
            logger.error(f"Download failed attempt {attempt}: {e}")
            time.sleep(1)

    logger.critical("Max retries reached. Download failed.")
    return False
