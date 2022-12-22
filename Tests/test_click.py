from Pages.click import Click
from Config.config import TestData


class TestCase():
    """Tests for the Click page"""

    def test_click(self, init_driver):
        self.click = Click(init_driver)
        class_before, class_after = self.click.go_click_and_get_class()
        assert class_before == TestData.click_class_before_expected
        assert class_after == TestData.click_class_after_expected
