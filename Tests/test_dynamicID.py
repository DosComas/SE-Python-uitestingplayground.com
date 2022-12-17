from Pages.dynamicID import DynamicID


class TestCase():
    """Tests for the Dynamic ID page"""

    def test_dynamic_id(self, init_driver):
        self.dynamicID = DynamicID(init_driver)
        assert self.dynamicID.go_and_click_btn() is True
