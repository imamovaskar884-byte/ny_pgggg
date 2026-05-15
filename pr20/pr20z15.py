class ChangeLogDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.name, "Не задано")
        print(f"Изменение {self.name}: {old_value} -> {value}")
        instance.__dict__[self.name] = value

class Record:
    data = ChangeLogDescriptor()

if __name__ == "__main__":
    r = Record()
    r.data = 10
    r.data = 20