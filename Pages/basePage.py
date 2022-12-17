from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class BasePage:
    """Parent class, funciones que heredan las demas paginas"""

    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # Methods
    def get_title(self):
        return self.driver.title

    def find_element_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def do_click(self, locator):
        element = self.find_element_xpath(locator)
        element.click()

    def do_send_keys(self, locator, value):
        element = self.find_element_xpath(locator)
        element.send_keys(value)

    def get_element_text(self, locator):
        element = self.find_element_xpath(locator)
        return element.text

    def scroll_into_view(self, locator):
        element = self.find_element_xpath(locator)
        return element.location_once_scrolled_into_view

    def find_elements_xpath(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def get_list_elements_xpath(self, locator):
        return [element.text for element in self.find_elements_xpath(locator)]

    def alert_accept(self):
        Alert(self.driver).accept()
