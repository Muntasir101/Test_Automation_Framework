import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.login_data import LoginTestData
import logging
from utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME
import time
import conftest
from utils.excel_utils import *

"""
Just Read data from excel file using pandas library
"""

# Implement Logging interface
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

# Create a file handler and set the logging level
file_handler = logging.FileHandler(LOGGING_FILENAME)
file_handler.setLevel(LOGGING_LEVEL)

# Create a formatter and add it to the file handler
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Implement Data Driven
# Define the path to your Excel file and sheet name
EXCEL_FILE = "./data/login_data.xlsx"
SHEET_NAME = "Sheet1"  # Update to match the name of your sheet


# Parametrize the test using the data from the Excel file
@pytest.mark.parametrize("username, password, expected_result", read_test_data(EXCEL_FILE, SHEET_NAME).values)
def test_login(setup, username, password, expected_result):
    logger.info("Starting the valid login test")
    login_page = LoginPage(setup)
    login_page.login(username, password)
    time.sleep(5)
    logger.info(f"Enter Username: {username}")
    logger.info(f"Enter Password: {password}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")

    if expected_result == "valid":
        # Add assertions for a successful login
        dashboard_page = DashboardPage(setup)
        try:
            assert dashboard_page.get_dashboard_text() == "Dashboard"
            actual_test_result = "Login successful"

        except:
            actual_test_result = "Unknown error occurred for valid"

    elif expected_result == "invalid":
        try:
            # Assert that an error message is displayed when the login is invalid.
            assert login_page.get_error_message() == "Invalid credentials"
            actual_test_result = "Error message displayed"

        except:
            actual_test_result = "Unknown error occurred for invalid"
    else:
        # Handle unexpected values in the Excel file
        raise ValueError(f"Unexpected expected_result: {expected_result}")


