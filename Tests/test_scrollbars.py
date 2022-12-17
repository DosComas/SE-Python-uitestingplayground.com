from Pages.scrollbars import Scrollbars


class TestCase():
    """Tests for the Scroll Bars page"""

    def test_scroll_bars(self, init_driver):
        self.scrollbars = Scrollbars(init_driver)
        assert self.scrollbars.go_locate_and_click_button() is not None
