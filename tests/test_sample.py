import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import URL
from utils.config import URL, BROWSER
from data.login_data import LoginTestData
import logging
from utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME
import time
import conftest

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


def test_valid_login(setup):
    logger.info("Starting the valid login test")
    login_page = LoginPage(setup)
    login_page.login(LoginTestData.VALID_USERNAME, LoginTestData.VALID_PASSWORD)
    time.sleep(5)
    logger.info(f"Enter Username: {LoginTestData.VALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.VALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")
    # Add assertions and further test steps
    dashboard_page = DashboardPage(setup)
    assert dashboard_page.get_dashboard_text() == "Dashboard"


def test_invalid_login(setup):
    logger.info("Starting the Invalid login test")
    login_page = LoginPage(setup)
    login_page.login(LoginTestData.INVALID_USERNAME, LoginTestData.INVALID_PASSWORD)
    time.sleep(5)
    logger.info(f"Enter Username: {LoginTestData.INVALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.INVALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")
    # Add assertions and further test steps
    # Assert that an error message is displayed when the login is invalid.
    assert login_page.get_error_message() == "Invalid credentials"
