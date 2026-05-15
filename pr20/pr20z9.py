class AccessCounterDescriptor:
    def __init__(self):
        self.count = 0

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.count += 1
        print(f"Обращений к атрибуту: {self.count}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass:
    data = AccessCounterDescriptor()

if __name__ == "__main__":
    obj = MyClass()
    obj.data = "Test"
    print(obj.data)
    print(obj.data)