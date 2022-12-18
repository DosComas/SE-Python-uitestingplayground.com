from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Parent class containing functions that the other pages inherit"""

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

    def check_existence(self, locator):
        try:
            self.find_element_xpath(locator)
            return True
        except NoSuchElementException:
            return False

    def check_clickable(self, locator):
        try:
            self.do_click(locator)
            return True
        except ElementClickInterceptedException:
            return False

    def check_visibility(self, locator):
        element = self.find_element_xpath(locator)
        return element.is_displayed()

    def wait_20s_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, locator)))

    def wait_20s_for_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator)))
