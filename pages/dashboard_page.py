from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.locators import DashboardPageLocators  # Import the locators


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_text = None

    def get_dashboard_text(self):
        self.dashboard_text = DashboardPageLocators.Dashboard
        dashboard_element = self.wait_for_element(*self.dashboard_text)
        return dashboard_element.text
