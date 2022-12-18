from Pages.ajax import AjaxData
from Config.config import TestData


class TestCase():
    """Tests for the AJAX Data page"""

    def test_ajax_data(self, init_driver):
        self.ajaxdata = AjaxData(init_driver)
        result = self.ajaxdata.go_click_and_get_text()
        assert result == TestData.ajax_data
