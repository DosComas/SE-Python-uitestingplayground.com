from Pages.dynamicid import DynamicID


class TestCase():
    """Tests for the Dynamic ID page"""

    def test_dynamic_id(self, init_driver):
        self.dynamicid = DynamicID(init_driver)
        assert self.dynamicid.go_and_click_btn() is True
