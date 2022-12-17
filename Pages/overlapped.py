from Pages.basePage import BasePage
from Config.config import TestData
from Config.locators import Locators


class Overlapped(BasePage):
    """Methods for interacting with the Overlapped Element page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_locate_and_input_name(self):
        self.do_click(Locators.overlapped_link)
        name_location = self.scroll_into_view(Locators.overlapped_name)
        self.do_send_keys(Locators.overlapped_name, TestData.overlapped_name)
        return name_location
