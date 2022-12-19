import pytest
from Pages.mouseover import MouseOver
from Config.config import TestData


class TestCase():
    """Tests for the Mouse Over page"""

    @pytest.mark.parametrize('input_clicks, expected_count',
                             TestData.mouseover_data)
    def test_mouse_over(self, init_driver, input_clicks, expected_count):
        self.mouseover = MouseOver(init_driver)
        count = self.mouseover.go_click_and_get_count(input_clicks)
        assert count == expected_count
