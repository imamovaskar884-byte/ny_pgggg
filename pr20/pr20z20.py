class ComplexDescriptor:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"[LOG] Чтение {self.name}")
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {self.name} должно быть int")
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Значение {self.name} вне диапазона [{self.min_val}, {self.max_val}]")
        
        print(f"[LOG] Установка {self.name} = {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"[LOG] Удаление атрибута {self.name} запрещено!")

class GameCharacter:
    health = ComplexDescriptor(0, 100)

if __name__ == "__main__":
    hero = GameCharacter()
    hero.health = 50       # Лог установки
    print(hero.health)     # Лог чтения
    
    try:
        del hero.health    # Ошибка удаления
    except AttributeError as e:
        print(e)