class EmailDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if '@' not in value:
            raise ValueError("Некорректный email. Отсутствует '@'")
        instance.__dict__[self.name] = value

class Person:
    email = EmailDescriptor()

if __name__ == "__main__":
    p = Person()
    
    p.email = "test@example.com"
    print(f"Успех! Email: {p.email}")
    
    try:
        p.email = "invalid_email.com"
    except ValueError as e:
        print(f"Ожидаемая ошибка поймана: {e}")