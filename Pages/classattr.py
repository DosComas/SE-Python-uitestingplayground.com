from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class ClassAttr(BasePage):
    """Methods for interacting with the Class Attribute page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_blue_btn_and_ok(self):
        self.do_click(Locators.class_attr_link)
        self.do_click(Locators.class_attr_btn)
        self.alert_accept()
        return True
