"""Pytest fixtures and hooks for Selenium WebDriver setup and screenshot capture on failure."""

import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from utils.config_reader import get_config
from utils.logger import setup_logger

@pytest.fixture(scope="function")
def setup(request):
    """Fixture to initialize and quit the WebDriver."""
    browser_type = get_config("default", "browser")

    try:
        if browser_type.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_type.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")
    except WebDriverException as exc:
        raise RuntimeError("WebDriver initialization failed.") from exc

    driver.maximize_window()
    request.node.driver = driver  # attach driver to test item

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, _):  # "_" to ignore unused 'call' argument
    """Hook to capture a screenshot when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)

            driver.save_screenshot(filepath)
            logger = setup_logger("test")
            logger.info("Screenshot saved to: %s", filepath)
