class Order:
    __slots__ = ('items',)

    def __init__(self, items):
        self.items = items

    def total_cost(self):
        return sum(self.items)

my_order = Order([150.50, 300, 45.20])
print(f"Общая стоимость заказа: {my_order.total_cost()}")
