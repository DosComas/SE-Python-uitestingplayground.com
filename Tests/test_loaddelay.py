from Pages.loaddelay import LoadDelay


class TestCase():
    """Tests for the Load Delay page"""

    def test_load_delay(self, init_driver):
        self.loaddelay = LoadDelay(init_driver)
        loaded = self.loaddelay.go_and_click_btn()
        assert loaded is True
