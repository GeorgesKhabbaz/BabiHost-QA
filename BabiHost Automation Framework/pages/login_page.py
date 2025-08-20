"""Page object model for the login page."""
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    """Page object for the login page."""

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")

    def enter_username(self, username):
        """Enter the username into the username field."""
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter the password into the password field."""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)
