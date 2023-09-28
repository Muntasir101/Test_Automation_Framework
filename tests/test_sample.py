import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import URL
from utils.config import URL, BROWSER
from data.login_data import LoginTestData
import logging
from utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME


@pytest.fixture
def setup():
    # You can use these variables in your test logic, e.g., opening the URL in a browser
    if BROWSER == "chrome":
        # Use Chrome WebDriver
        driver = webdriver.Chrome()
    elif BROWSER == "firefox":
        # Use Firefox WebDriver
        driver = webdriver.Firefox()
    else:
        # Handle unsupported browsers or configurations
        raise ValueError("Unsupported browser:", BROWSER)

    driver.get(URL)

    yield driver
    driver.quit()

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
    logger.info(f"Enter Username: {LoginTestData.VALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.VALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")
    # Add assertions and further test steps

def test_invalid_login(setup):
    logger.info("Starting the Invalid login test")
    login_page = LoginPage(setup)
    login_page.login(LoginTestData.INVALID_USERNAME, LoginTestData.INVALID_PASSWORD)
    logger.info(f"Enter Username: {LoginTestData.INVALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.INVALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")
    # Add assertions and further test steps
