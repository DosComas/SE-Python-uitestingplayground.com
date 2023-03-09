import pytest
from os import path
from selenium import webdriver
from Config.config import TestData

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Instantiate the browser session and drop it
@pytest.fixture(params=TestData.browser, scope="class")
def init_driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    if request.param == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(
            GeckoDriverManager().install(),
            log_path=path.devnull,
        ))
        driver.maximize_window()

    if request.param == "Edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.maximize_window()

    yield driver
    driver.quit()


# Instantiate the browser session ignoring the certificates and drop it
@pytest.fixture(params=TestData.browser, scope="class")
def init_driver_ignore(request):
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
        driver.maximize_window()

    if request.param == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install(),
                log_path=path.devnull,
            ),
            options=options,
        )
        driver.maximize_window()

    if request.param == "Edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options,
        )
        driver.maximize_window()

    yield driver
    driver.quit()
