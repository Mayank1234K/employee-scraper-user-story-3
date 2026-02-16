import pandas as pd
import logging
from .validator import validate_structure, validate_missing_data

logger = logging.getLogger(__name__)

def parse_excel(file_path):
    try:
        df = pd.read_excel(file_path)

        if not validate_structure(df):
            return None

        validate_missing_data(df)

        return df

    except Exception as e:
        logger.error(f"Parsing failed: {e}")
        return None
