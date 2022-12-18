from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class ClientSideDelay(BasePage):
    """Methods for interacting with the Client Side Delay page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_and_get_text(self):
        self.do_click(Locators.clientdelay_link)
        self.do_click(Locators.clientdelay_btn)
        self.wait_20s_for_element_to_disappear(Locators.clientdelay_spinner)
        return self.get_element_text(Locators.clientdelay_text)
