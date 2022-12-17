from Pages.dynamictable import DynamicTable


class TestCase():
    """Tests for the Dynamic Table page"""

    def test_dynamic_table(self, init_driver):
        self.dynamictable = DynamicTable(init_driver)
        self.dynamictable.go_to_page()
        table_cpu = self.dynamictable.get_table_cpu()
        yellow_cpu = self.dynamictable.get_yellow_cpu()
        assert table_cpu == yellow_cpu
