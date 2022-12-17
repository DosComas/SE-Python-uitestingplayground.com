from Pages.basePage import BasePage
from Config.config import TestData
from Config.locators import Locators


class DynamicTable(BasePage):
    """Methods for specifically interacting with the Dynamic Table page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_to_page(self):
        self.do_click(Locators.dynamic_table_link)

    def get_table_cpu(self):
        headers = self.get_list_elements_xpath(Locators.dynamic_table_headers)
        cells = self.get_list_elements_xpath(Locators.dynamic_table_cells)
        return cells[headers.index('CPU') + cells.index('Chrome')]

    def get_yellow_cpu(self):
        text = self.get_element_text(Locators.dynamic_table_yellow)
        return text.replace('Chrome CPU: ', '')
