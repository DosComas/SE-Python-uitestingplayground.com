from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class AjaxData(BasePage):
    """Methods for interacting with the AJAX Data page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_and_get_text(self):
        self.do_click(Locators.ajax_link)
        self.do_click(Locators.ajax_btn)
        response = self.wait_20s_for_presence_of_element(Locators.ajax_text)
        return response.text
