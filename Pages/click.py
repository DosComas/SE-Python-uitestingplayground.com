from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators


class Click(BasePage):
    """Methods for interacting with the Click page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_and_get_class(self):
        self.do_click(Locators.click_link)
        btn = self.find_element_xpath(Locators.click_btn)
        class_before = btn.get_attribute("class")
        btn.click()
        class_after = btn.get_attribute("class")
        return class_before, class_after
