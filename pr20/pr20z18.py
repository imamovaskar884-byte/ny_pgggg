class NumberListDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Должен быть список")
        if not all(isinstance(x, (int, float)) for x in value):
            raise ValueError("Список должен содержать только числа")
        instance.__dict__[self.name] = value

class Dataset:
    values = NumberListDescriptor()

if __name__ == "__main__":
    d = Dataset()
    
    d.values = [1, 2, 3.5]
    print(f"Успех! Данные: {d.values}")
    
    try:
        d.values = [1, "два"]
    except ValueError as e:
        print(f"Ожидаемая ошибка поймана: {e}")