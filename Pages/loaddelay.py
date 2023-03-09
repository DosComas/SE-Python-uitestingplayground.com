from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class LoadDelay(BasePage):
    """Methods for interacting with the Load Delay page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_click_btn(self):
        self.do_click(Locators.load_delay_link)
        btn = self.wait_20s_for_presence_of_element(Locators.load_delay_btn)
        btn.click()
        return True
