class Animal:
    __slots__ = ('type', 'weight')

a = Animal()
a.type = "Кот"
a.weight = 5

try:
    a.color = "Рыжий"
except AttributeError as e:
    print(f"Что произошло: возникла ошибка '{e}', так как слоты запрещают добавление атрибута 'color'.")

