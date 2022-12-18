from Pages.clientdelay import ClientSideDelay
from Config.config import TestData


class TestCase():
    """Tests for the Client Side Delay page"""

    def test_client_side_delay(self, init_driver):
        self.clientdelay = ClientSideDelay(init_driver)
        result = self.clientdelay.go_click_and_get_text()
        assert result == TestData.clientdelay_data
