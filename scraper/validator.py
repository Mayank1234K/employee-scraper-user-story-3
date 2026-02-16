import logging

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "Employee ID",
    "First Name",
    "Last Name",
    "Email",
    "Job Title",
    "Phone Number",
    "Hire Date"
]

def validate_structure(df):
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            logger.error(f"Missing column: {col}")
            return False
    return True


def validate_missing_data(df):
    if df[REQUIRED_COLUMNS].isnull().any().any():
        logger.warning("Missing values found")
        return False
    return True
