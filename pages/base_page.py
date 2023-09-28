from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """
    A base class for page objects with common utility methods.

    Args:
        driver: The Selenium WebDriver instance.

    Attributes:
        driver: The Selenium WebDriver instance associated with the page.
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """
        Wait for an element to be present on the page.

        Args:
            by: The method to locate the element (e.g., By.ID, By.NAME, By.XPATH).
            value: The value to locate the element by.
            timeout (int): The maximum time (in seconds) to wait for the element.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: The located element.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, by, value):
        """
        Click on an element after waiting for it to be present.

        Args:
            by: The method to locate the element (e.g., By.ID, By.NAME, By.XPATH).
            value: The value to locate the element by.
        """
        element = self.wait_for_element(by, value)
        element.click()

    def input_text(self, by, value, text):
        """
        Input text into an input field after waiting for it to be present.

        Args:
            by: The method to locate the input field (e.g., By.ID, By.NAME, By.XPATH).
            value: The value to locate the input field by.
            text (str): The text to be input into the field.
        """
        element = self.wait_for_element(by, value)
        element.send_keys(text)
