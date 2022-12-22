from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class VerifyText(BasePage):
    """Methods for interacting with the Verify Text page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_get_text(self):
        self.do_click(Locators.verifytext_link)
        return self.get_element_text(Locators.verifytext_text)
