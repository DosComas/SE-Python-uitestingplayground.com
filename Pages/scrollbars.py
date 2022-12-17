from Pages.base_page import BasePage
from Config.config import TestData
from Config.locators import Locators


class Scrollbars(BasePage):
    """Methods for interacting with the Scroll Bars page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_locate_and_click_button(self):
        self.do_click(Locators.scrollbars_link)
        button_location = self.scroll_into_view(Locators.scrollbars_btn)
        self.do_click(Locators.scrollbars_btn)
        return button_location
