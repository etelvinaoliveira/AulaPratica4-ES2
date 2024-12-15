import pytest
from Item import Item

class TestItems:
    def test_valid_item_creation(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "high")
        assert item.name == "Produto A"
        assert item.description == "Descrição do Produto A"
        assert item.quantity == 10
        assert item._priority == "high"

    def test_negative_quantity_on_item_creation(self):
        with pytest.raises(ValueError, match="A quantidade não pode ser negativa."):
            Item("Produto A", "Descrição do Produto A", -5, "medium")

    def test_invalid_priority_on_item_creation(self):
        with pytest.raises(ValueError, match="Prioridade deve ser 'low', 'medium' ou 'high'."):
            Item("Produto A", "Descrição do Produto A", 10, "urgente")

    def test_valid_quantity_update(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "medium")
        item.update_quantity(20)
        assert item.quantity == 20

    def test_negative_quantity_update(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "medium")
        with pytest.raises(ValueError, match="A quantidade não pode ser negativa."):
            item.update_quantity(-5)

    def test_valid_priority_update(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "medium")
        item.update_priority("high")
        assert item._priority == "high"

    def test_invalid_priority_update(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "medium")
        with pytest.raises(ValueError, match="Prioridade deve ser 'low', 'medium' ou 'high'."):
            item.update_priority("urgente")

    def test_str_representation(self):
        item = Item("Produto A", "Descrição do Produto A", 10, "high")
        expected_str = "Produto: Produto A\nDescrição: Descrição do Produto A\nQuantidade: 10\nPrioridade: High"
        assert str(item) == expected_str
