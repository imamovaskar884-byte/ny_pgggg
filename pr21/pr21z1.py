class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = "Иван"
p.age = 20
print(f"Имя: {p.name}, Возраст: {p.age}")
