from Pages.classattr import ClassAttr


class TestCase():
    """Tests for the Class Attribute page"""

    def test_class_attribute(self, init_driver):
        self.classArrt = ClassAttr(init_driver)
        assert self.classArrt.go_click_blue_btn_and_ok() is True
