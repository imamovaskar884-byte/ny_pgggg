class StringDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")
        instance.__dict__[self.name] = value

class MyClass:
    text = StringDescriptor()

if __name__ == "__main__":
    obj = MyClass()
    obj.text = "Привет"
    # obj.text = 123 # Вызовет TypeError