import pytest
from ShoppingList import ShoppingList
from Item import Item

class TestShoppingList:
    
    @pytest.fixture
    def shopping_list(self):
        return ShoppingList()

    def test_add_item(self, shopping_list):
        high_priority_item = Item("Produto A", "Descrição do Produto A", 5, "high")
        shopping_list.add_item(high_priority_item)
        assert shopping_list.total_items() == 1
        assert high_priority_item in shopping_list.items['high']

    def test_remove_item(self, shopping_list):
        high_priority_item = Item("Produto A", "Descrição do Produto A", 5, "high")
        shopping_list.add_item(high_priority_item)
        shopping_list.remove_item("Produto A")
        assert shopping_list.total_items() == 0
        assert high_priority_item not in shopping_list.items['high']

    def test_remove_non_existent_item(self, shopping_list):
        initial_count = shopping_list.total_items()
        shopping_list.remove_item("Produto Inexistente")
        assert shopping_list.total_items() == initial_count

    def test_update_item_quantity(self, shopping_list):
        high_priority_item = Item("Produto A", "Descrição do Produto A", 5, "high")
        shopping_list.add_item(high_priority_item)
        shopping_list.update_item("Produto A", quantity=10)
        assert high_priority_item.quantity == 10

    def test_update_item_priority(self, shopping_list):
        medium_priority_item = Item("Produto B", "Descrição do Produto B", 3, "medium")
        shopping_list.add_item(medium_priority_item)
        shopping_list.update_item("Produto B", priority="high")
        assert medium_priority_item in shopping_list.items['high']
        assert medium_priority_item not in shopping_list.items['medium']

    def test_update_non_existent_item(self, shopping_list):
        initial_count = shopping_list.total_items()
        shopping_list.update_item("Produto Inexistente", quantity=5)
        assert shopping_list.total_items() == initial_count

    def test_search_item(self, shopping_list):
        high_priority_item = Item("Produto A", "Descrição do Produto A", 5, "high")
        shopping_list.add_item(high_priority_item)
        result = shopping_list.search_item("Produto A")
        assert result == high_priority_item

    def test_search_non_existent_item(self, shopping_list):
        result = shopping_list.search_item("Produto Inexistente")
        assert result is None

    def test_search_items_by_priority(self, shopping_list):
        high_priority_item = Item("Produto A", "Descrição do Produto A", 5, "high")
        medium_priority_item = Item("Produto B", "Descrição do Produto B", 3, "medium")
        shopping_list.add_item(high_priority_item)
        shopping_list.add_item(medium_priority_item)
        items_high = shopping_list.search_items_priority("high")
        items_medium = shopping_list.search_items_priority("medium")
        assert len(items_high) == 1
        assert high_priority_item in items_high
        assert len(items_medium) == 1
        assert medium_priority_item in items_medium

    def test_display_empty_list(self, shopping_list):
        with pytest.raises(ValueError, match="A lista de compras está vazia."):
            shopping_list.display_list()
