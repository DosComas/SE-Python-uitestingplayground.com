from Pages.visibility import Visibility


class TestCase():
    """Tests for the Visibility page"""

    def test_visibility(self, init_driver):
        self.visibility = Visibility(init_driver)
        self.visibility.go_and_hide_btn()
        assert self.visibility.check_removed_btn() is False
        assert self.visibility.check_zero_width_btn() is False
        assert self.visibility.check_overlapped_btn() is False
        assert self.visibility.check_opacity_0_btn() is False
        assert self.visibility.check_hidden_btn() is False
        assert self.visibility.check_display_none_btn() is False
        assert self.visibility.check_offscreen_btn() is False
