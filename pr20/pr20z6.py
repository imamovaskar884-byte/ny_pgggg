class PositiveNumberDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Значение должно быть положительным")
        instance.__dict__[self.name] = value

class MyClass:
    score = PositiveNumberDescriptor()

if __name__ == "__main__":
    obj = MyClass()
    
    obj.score = 10
    print(f"Успех! score = {obj.score}")
    
    try:
        obj.score = -5
    except ValueError as e:
        print(f"Ожидаемая ошибка поймана: {e}")