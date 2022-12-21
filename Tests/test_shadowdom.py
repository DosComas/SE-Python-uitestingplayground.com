from Pages.shadowdom import ShadowDOM


class TestCase():
    """Tests for the Shadow DOM page"""

    def test_shadow_dom(self, init_driver_ignore):
        self.shadowdom = ShadowDOM(init_driver_ignore)
        self.shadowdom.go_to_page_and_generate()
        expected_result = self.shadowdom.get_input_field()
        result = self.shadowdom.get_clipboard()
        assert result == expected_result
