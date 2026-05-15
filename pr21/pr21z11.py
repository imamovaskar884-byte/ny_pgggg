class Product:
    __slots__ = ('name', '_price')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Ошибка: Цена не может быть отрицательной! Установлено значение 0.")
            self._price = 0
        else:
            self._price = value

prod = Product("Ноутбук", -1500)
prod.price = 1200
print(f"Товар: {prod.name}, Итоговая цена: {prod.price}")
