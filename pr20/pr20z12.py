class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or not (0 <= value <= 120):
            raise ValueError("Возраст должен быть от 0 до 120")
        instance.__dict__[self.name] = value

class Person:
    age = AgeDescriptor()

if __name__ == "__main__":
    p = Person()
    
    p.age = 25
    print(f"Успех! Возраст: {p.age}")
    
    try:
        p.age = 150
    except ValueError as e:
        print(f"Ожидаемая ошибка поймана: {e}")