"""Base page module for common Selenium actions."""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        """
        Initialize the BasePage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.timeout = 10

    def click(self, by_locator):
        """
        Click on the element located by the given locator.

        :param by_locator: Locator tuple (By, locator)
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, value):
        """
        Send keys to the element located by the given locator.

        :param by_locator: Locator tuple (By, locator)
        :param value: Text to send
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        """
        Get text from the element located by the given locator.

        :param by_locator: Locator tuple (By, locator)
        :return: Text of the element
        """
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """
        Check if the element located by the given locator is visible.

        :param by_locator: Locator tuple (By, locator)
        :return: True if visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False
