from Pages.scrollbars import Scrollbars


class TestCase():
    """Tests for the Scrollbars page"""

    def test_scrollbars(self, init_driver):
        self.scrollbars = Scrollbars(init_driver)
        assert self.scrollbars.go_locate_and_click_button() is not None
