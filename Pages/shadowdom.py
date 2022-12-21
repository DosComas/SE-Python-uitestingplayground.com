from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators
import tkinter as tk


class ShadowDOM(BasePage):
    """Methods for interacting with the Shadow DOM page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url_ssl)

    def go_to_page_and_generate(self):
        self.do_click(Locators.shadowdom_link)
        gen_btn = self.find_element_shadow_root(
            Locators.shadowdom_script_gen_btn)
        gen_btn.click()

    def get_clipboard(self):
        copy_btn = self.find_element_shadow_root(
            Locators.shadowdom_script_copy_btn)
        copy_btn.click()
        return tk.Tk().clipboard_get()

    def get_input_field(self):
        input_field = self.find_element_shadow_root(
            Locators.shadowdom_script_input_field)
        return input_field.get_attribute('value')
