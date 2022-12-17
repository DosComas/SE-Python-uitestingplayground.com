from Pages.loadDelay import LoadDelay


class TestCase():
    """Tests for the Load Delay page"""

    def test_loadDelay(self, init_driver):
        self.loadDelay = LoadDelay(init_driver)
        assert self.loadDelay.go_and_click_btn() is True
