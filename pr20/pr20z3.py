class LogSetDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print("Setting value")
        instance.__dict__[self.name] = value

class MyClass:
    attr = LogSetDescriptor()

if __name__ == "__main__":
    obj = MyClass()
    obj.attr = 100