"""Page object model for the home page."""

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    """Page object for the home page."""

    DASHBOARD_TEXT = (By.TAG_NAME, "h1")

    def is_dashboard_visible(self):
        """Check if the dashboard header is visible."""
        return self.is_visible(self.DASHBOARD_TEXT)
