import re
from Pages.base_page import BasePage
from Config.config import TestData
from Config.locators import Locators


class ProgressBar(BasePage):
    """Methods for interacting with the Progress Bar page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_get_result(self):
        self.do_click(Locators.progress_bar_link)
        self.do_click(Locators.progress_bar_start)
        bar = self.find_element_xpath(Locators.progress_bar_bar)
        while True:
            progress = bar.get_attribute('aria-valuenow')
            if progress == '75':
                self.do_click(Locators.progress_bar_stop)
                result = self.find_element_xpath(Locators.progress_bar_result)
                regex = r'^(?:Result: )(.*)(?:, duration: \d*)$'
                return re.search(regex, result.text).group(1)
