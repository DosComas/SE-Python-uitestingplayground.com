from Pages.hiddenlayers import HiddenLayers
from Config.config import TestData


class TestCase():
    """Tests for the Hidden Layers page"""

    def test_hidden_layers(self, init_driver):
        self.hiddenlayers = HiddenLayers(init_driver)
        clickable = self.hiddenlayers.go_click_and_check()
        assert clickable is False
