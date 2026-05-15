class MaxLengthDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Должна быть строка")
        if len(value) > 10:
            raise ValueError("Длина не более 10 символов")
        instance.__dict__[self.name] = value

class User:
    username = MaxLengthDescriptor()

if __name__ == "__main__":
    u = User()
    
    u.username = "Admin"
    print(f"Успех! Имя пользователя: {u.username}")
    
    try:
        u.username = "VeryLongUsername123"
    except ValueError as e:
        print(f"Ожидаемая ошибка поймана: {e}")