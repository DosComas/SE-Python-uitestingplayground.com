import pytest
from Pages.textInput import TextInput
from Config.config import TestData


class TestCase():
    """Tests for the Text Input page"""

    @pytest.mark.parametrize('input_text, expected_result',
                             TestData.text_input_field_data)
    def test_text_input(self, init_driver, input_text, expected_result):
        self.textInput = TextInput(init_driver)
        text = self.textInput.go_and_do_input(input_text)
        assert text == expected_result
