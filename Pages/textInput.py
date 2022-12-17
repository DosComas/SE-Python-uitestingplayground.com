from Pages.basePage import BasePage
from Config.config import TestData
from Config.locators import Locators


class TextInput(BasePage):
    """Methods for interacting with the Text Input page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_and_do_input(self, input_field):
        self.do_click(Locators.text_input_link)
        self.do_send_keys(Locators.text_input_name, input_field)
        self.do_click(Locators.text_input_btn)
        return self.get_element_text(Locators.text_input_btn)
