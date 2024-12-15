class Item:
    def __init__(self, name, description, quantity, priority):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if priority not in ['low', 'medium', 'high']:
            raise ValueError("Prioridade deve ser 'low', 'medium' ou 'high'.")
        
        self._name = name
        self._description = description
        self._quantity = quantity
        self._priority = priority

    def __str__(self):
        return f'Produto: {self.name}\nDescrição: {self.description}\nQuantidade: {self.quantity}\nPrioridade: {self.priority.capitalize()}'

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @property
    def quantity(self):
        return self._quantity

    @property
    def priority(self):
        return self._priority

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantity = quantity
        print(f'Quantidade do produto "{self._name}" atualizada para {self._quantity}.')

    def update_priority(self, priority):
        if priority not in ['low', 'medium', 'high']:
            raise ValueError("Prioridade deve ser 'low', 'medium' ou 'high'.")
        self._priority = priority
        print(f'Prioridade do produto "{self._name}" atualizada para {self._priority.capitalize()}.')