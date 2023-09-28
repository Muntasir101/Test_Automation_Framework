from selenium.webdriver.common.by import By

class LoginPageLocators:
    """
    Locators for elements on the login page.
    """
    # Define locators
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")

class DashboardPageLocators:
    """
    Locators for elements on the dashboard page.
    """
    Dashboard = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module")
