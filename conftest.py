import pytest
from selenium import webdriver
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
