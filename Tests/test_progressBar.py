from Pages.progressBar import ProgressBar
from Config.config import TestData


class TestCase():
    """Tests for the Progress Bar page"""

    def test_progressBar(self, init_driver):
        self.progressBar = ProgressBar(init_driver)
        result = self.progressBar.go_and_get_result()
        assert result == TestData.progress_bar_result
