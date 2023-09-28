import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import URL
from utils.config import URL, BROWSER

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


def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin", "admin123")
    # Add assertions and further test steps

def test_login_invalid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin invalid", "admin123")
    # Add assertions and further test steps
