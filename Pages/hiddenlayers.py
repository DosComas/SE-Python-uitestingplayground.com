from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class HiddenLayers(BasePage):
    """Methods for interacting with the Hidden Layers page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_and_check(self):
        self.do_click(Locators.hiddenlayers_link)
        self.do_click(Locators.hiddenlayers_green_btn)
        self.do_click(Locators.hiddenlayers_blue_btn)
        return self.check_clickable(Locators.hiddenlayers_green_btn)
