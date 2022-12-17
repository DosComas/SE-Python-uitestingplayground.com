from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class SampleApp(BasePage):
    """Methods for interacting with the Sample App page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_do_login(self, username, password):
        self.do_click(Locators.sample_app_link)
        self.do_send_keys(Locators.sample_app_user, username)
        self.do_send_keys(Locators.sample_app_pass, password)
        self.do_click(Locators.sample_app_login)
        welcome_text = self.get_element_text(Locators.sample_app_welcome)
        self.do_click(Locators.sample_app_login)
        return welcome_text
