import pytest
from Pages.sampleapp import SampleApp
from Config.config import TestData


class TestCase():
    """Tests for the Sample App page"""

    @pytest.mark.parametrize('username, password, expected_result',
                             TestData.sample_app_login_data)
    def test_sample_app(self, init_driver, username, password,
                        expected_result):
        self.sampleapp = SampleApp(init_driver)
        text = self.sampleapp.go_and_do_login(username, password)
        assert text == expected_result
