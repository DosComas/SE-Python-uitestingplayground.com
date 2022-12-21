import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData


# Instantiate the browser session and drop it
@pytest.fixture(scope="class")
def init_driver():
    if TestData.browser == "Chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Instantiate the browser session ignoring the certificates and drop it
@pytest.fixture(scope="class")
def init_driver_ignore():
    if TestData.browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    yield driver
    driver.quit()
