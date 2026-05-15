class ClassWithSlots:
    __slots__ = ('name',)

class ClassWithoutSlots:
    pass

obj1 = ClassWithSlots()
obj1.name = "Тест 1"
try:
    obj1.new_attr = 100
except AttributeError:
    print("Вывод: В объект со слотами добавить новый атрибут нельзя.")

obj2 = ClassWithoutSlots()
obj2.new_attr = 100
print(f"Вывод: В объект без слотов успешно добавлен атрибут со значением {obj2.new_attr}.")
