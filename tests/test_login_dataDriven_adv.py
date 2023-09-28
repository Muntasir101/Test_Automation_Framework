import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import logging
from config.configuration import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME
import time
from utils.excel_utils import *

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

# Define the path to your Excel file and sheet name
EXCEL_FILE = "./data/login_data.xlsx"
SHEET_NAME = "Sheet1"  # Update to match the name of your sheet

# Initialize an empty list to store the test results
test_results = []


# Parametrize the test using the data from the Excel file
@pytest.mark.parametrize("username, password, expected_result",
                         read_test_data(EXCEL_FILE, SHEET_NAME).values)
def test_login(setup, username, password, expected_result):
    """
    Perform login tests using data from an Excel file.

    Args:
        setup: The test setup including the WebDriver instance.
        username (str): The username for the login attempt.
        password (str): The password for the login attempt.
        expected_result (str): The expected result ('valid' or 'invalid').

    Returns:
        None
    """
    logger.info("Starting the login test")
    login_page = LoginPage(setup)
    login_page.login(username, password)
    time.sleep(5)
    logger.info(f"Enter Username: {username}")
    logger.info(f"Enter Password: {password}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")

    if expected_result == "valid":
        dashboard_page = DashboardPage(setup)
        try:
            assert dashboard_page.get_dashboard_text() == "Dashboard"
            actual_test_result = "Login successful"
        except AssertionError:
            actual_test_result = "Unknown error occurred for valid"

    elif expected_result == "invalid":
        try:
            assert login_page.get_error_message() == "Invalid credentials"
            actual_test_result = "Error message displayed"
        except AssertionError:
            actual_test_result = "Unknown error occurred for invalid"
    else:
        raise ValueError(f"Unexpected expected_result: {expected_result}")

    # Append the actual test result to the list
    test_results.append(actual_test_result)


# After all tests have run, write the test results to the Excel file
@pytest.fixture(scope="session", autouse=True)
def write_test_results_to_excel(request):
    """
    Fixture to write the test results to an Excel file after all tests have run.

    Args:
        request: The Pytest request object.

    Returns:
        None
    """
    def finalize():
        # Load the existing Excel file
        existing_data = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

        # Add the test results as a new column
        existing_data['Actual Result'] = test_results

        # Save the updated DataFrame back to the same Excel file
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
            existing_data.to_excel(writer, sheet_name=SHEET_NAME, index=False)

    request.addfinalizer(finalize)
