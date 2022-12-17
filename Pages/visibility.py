from Pages.base_page import BasePage
from Config.config import TestData
from Config.locators import Locators


class Visibility(BasePage):
    """Methods for interacting with the Visibility page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_hide_btn(self):
        self.do_click(Locators.visibility_link)
        self.do_click(Locators.visibility_hide_btn)

    def check_removed_btn(self):
        return self.check_existence(Locators.visibility_removed_btn)

    def check_zero_width_btn(self):
        return self.check_visibility(Locators.visibility_zero_width_btn)

    def check_overlapped_btn(self):
        return self.check_clickable(Locators.visibility_overlapped_btn)

    def check_opacity_0_btn(self):
        return self.check_visibility(Locators.visibility_opacity_0_btn)

    def check_hidden_btn(self):
        return self.check_visibility(Locators.visibility_hidden_btn)

    def check_display_none_btn(self):
        return self.check_visibility(Locators.visibility_display_none_btn)

    def check_offscreen_btn(self):
        return self.check_visibility(Locators.visibility_offscreen_btn)
