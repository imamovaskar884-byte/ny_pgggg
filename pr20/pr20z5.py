class IntDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Значение должно быть типа int")
        instance.__dict__[self.name] = value

class MyClass:
    number = IntDescriptor()

if __name__ == "__main__":
    obj = MyClass()
    
    # 1. Успешная запись
    obj.number = 5   
    print(f"Успех! number = {obj.number}")
    
    # 2. Проверка ошибки
    try:
        obj.number = "5"
    except TypeError as e:
        print(f"Ожидаемая ошибка поймана: {e}")