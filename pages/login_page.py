from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.locators import LoginPageLocators  # Import the locators

class LoginPage(BasePage):

    def login(self, username, password):
        # Use the locators from LoginPageLocators
        self.input_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
