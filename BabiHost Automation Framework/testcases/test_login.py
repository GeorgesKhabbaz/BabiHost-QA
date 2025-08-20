"""Tests for login functionality using data-driven approach."""
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.excel_reader import get_login_data

@pytest.mark.parametrize("username,password,expected", get_login_data())
def test_login(setup, username, password, expected):
    """Test login functionality with different credentials."""
    driver = setup
    driver.get("https://example.com/login")  # Consider using config

    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    home = HomePage(driver)

    if expected == "Pass":
        assert home.is_dashboard_visible()
    else:
        assert not home.is_dashboard_visible()
