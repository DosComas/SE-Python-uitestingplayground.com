import pytest
from Pages.sampleApp import SampleApp
from Config.config import TestData


class TestCase():
    """Tests for the Sample App page"""

    @pytest.mark.parametrize('username, password, expected_result',
                             TestData.sample_app_login_data)
    def test_sample_app(self, init_driver, username, password, expected_result):
        self.sampleApp = SampleApp(init_driver)
        text = self.sampleApp.go_and_do_login(username, password)
        assert text == expected_result
