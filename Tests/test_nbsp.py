from Pages.nbsp import NBSP


class TestCase():
    """Tests for the Non-Breaking Space page"""

    def test_non_breaking_space(self, init_driver):
        self.nbsp = NBSP(init_driver)
        assert self.nbsp.go_and_click_btn() is True
