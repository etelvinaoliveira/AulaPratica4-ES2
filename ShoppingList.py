from Item import Item

class ShoppingList:
    def __init__(self):
        self._items =  {
            'low': [],
            'medium': [],
            'high': []
        }

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self.items[item.priority].append(item)
        print(f'Item "{item.name}" adicionado à lista de compras.')

    def total_items(self):
        return sum(len(item_list) for item_list in self.items.values())

    def remove_item(self, item_name):
        for priority in self.items:
            for item in self.items[priority]:
                if item.name == item_name:
                    self.items[priority].remove(item)
                    print(f'Item "{item_name}" removido da lista de compras.')
                    return
        print(f'Item "{item_name}" não encontrado na lista de compras.')

    def update_item(self, item_name, quantity=None, priority=None):
        for current_priority in self._items:
            for item in self._items[current_priority]:
                if item.name == item_name:
                    if quantity is not None:
                        item.update_quantity(quantity)

                    if priority is not None and priority != current_priority:
                        if priority not in self._items:
                            raise ValueError("Prioridade inválida. Deve ser 'low', 'medium' ou 'high'.")
                        self._items[current_priority].remove(item)
                        item.update_priority(priority)
                        self._items[priority].append(item)

                    return

        print(f'Item "{item_name}" não encontrado na lista de compras.')

    def search_item(self, item_name):
        for priority in self.items:
            for item in self.items[priority]:
                if item.name == item_name:
                    return item
        print(f"Item: {item_name} não encontrado")

    def search_items_priority(self, priority):
        return self.items[priority]

    def display_list(self):
        if all(len(lst) == 0 for lst in self.items.values()):
            raise ValueError("A lista de compras está vazia.")
        else:
            print("Lista de compras:")
            for priority in ['high', 'medium', 'low']:
                if self.items[priority]:
                    print(f'\nPrioridade {priority.capitalize()}:')
                    for item in self.items[priority]:
                        print(item)
                        print('---')
