from Pages.progressbar import ProgressBar
from Config.config import TestData


class TestCase():
    """Tests for the Progress Bar page"""

    def test_progress_bar(self, init_driver):
        self.progressbar = ProgressBar(init_driver)
        result = self.progressbar.go_and_get_result()
        assert result in TestData.progress_bar_result
