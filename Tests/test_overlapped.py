from Pages.overlapped import Overlapped


class TestCase():
    """Tests for the Overlapped Element page"""

    def test_overlapped_element(self, init_driver):
        self.overlapped = Overlapped(init_driver)
        assert self.overlapped.go_locate_and_input_name() is not None
