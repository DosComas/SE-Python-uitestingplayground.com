from Pages.verifytext import VerifyText
from Config.config import TestData


class TestCase():
    """Tests for the Verify Text page"""

    def test_verify_text(self, init_driver):
        self.verifytext = VerifyText(init_driver)
        result = self.verifytext.go_and_get_text()
        assert result == TestData.verifytext_expected
