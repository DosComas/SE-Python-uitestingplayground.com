from Pages.basepage import BasePage
from Config.config import TestData
from Config.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class MouseOver(BasePage):
    """Methods for interacting with the Mouse Over page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_click_and_get_count(self, number):
        self.do_click(Locators.mouseover_link)
        click_me = self.find_element_xpath(Locators.mouseover_click_me)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_me)
        [f() for f in [actions.click] * number]
        actions.perform()

        return self.get_element_text(Locators.mouseover_count)
