from Pages.dynamictable import DynamicTable


class TestCase():
    """Tests for the Dynamic Table page"""

    def test_dynamic_table(self, init_driver):
        self.dynamicTable = DynamicTable(init_driver)
        self.dynamicTable.go_to_page()
        table_cpu = self.dynamicTable.get_table_cpu()
        yellow_cpu = self.dynamicTable.get_yellow_cpu()
        assert table_cpu == yellow_cpu
