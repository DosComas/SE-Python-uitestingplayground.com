from Pages.loaddelay import LoadDelay


class TestCase():
    """Tests for the Load Delay page"""

    def test_load_delay(self, init_driver):
        self.loadDelay = LoadDelay(init_driver)
        assert self.loadDelay.go_and_click_btn() is True
