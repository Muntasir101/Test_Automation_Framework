from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.locators import LoginPageLocators  # Import the locators

class LoginPage(BasePage):
    """
    Page object class representing the login page.

    Args:
        driver: The Selenium WebDriver instance.

    Attributes:
        error_message: Locator for the error message element.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.error_message = None

    def login(self, username, password):
        """
        Perform a login action using the provided username and password.

        Args:
            username (str): The username for the login attempt.
            password (str): The password for the login attempt.
        """
        # Use the locators from LoginPageLocators
        self.input_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Get the error message displayed on the login page.

        Returns:
            str: The text of the error message.
        """
        self.error_message = LoginPageLocators.ERROR_MESSAGE
        error_message_element = self.wait_for_element(*self.error_message)
        return error_message_element.text
