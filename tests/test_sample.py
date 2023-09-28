import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import URL

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()

def test_login(setup):
    login_page = LoginPage(setup)
    login_page.login("your_username", "your_password")
    # Add assertions and further test steps
