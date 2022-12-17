from Pages.basePage import BasePage
from Config.config import TestData
from Config.locators import Locators


class LoadDelay(BasePage):
    """Methods for interacting with the Sample App page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_click_btn(self):
        self.do_click(Locators.load_delay_link)
        self.do_click(Locators.load_delay_button)
        return True
