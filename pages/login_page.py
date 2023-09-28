from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Define locators using By class
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")

    def login(self, username, password):
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)
