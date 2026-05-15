class PrivateStorageDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass:
    data = PrivateStorageDescriptor()

if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    obj1.data = "Секрет 1"
    obj2.data = "Секрет 2"
    
    print(obj1.__dict__)  # Вывод: {'data': 'Секрет 1'}
    print(obj2.__dict__)  # Вывод: {'data': 'Секрет 2'}