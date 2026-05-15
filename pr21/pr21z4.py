class Car:
    __slots__ = ('brand', 'model', 'year')

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

c = Car("Toyota", "Corolla", 2020)
print(f"Автомобиль: {c.brand} {c.model}, Год выпуска: {c.year}")
