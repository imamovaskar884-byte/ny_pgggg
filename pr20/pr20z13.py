class RoundedDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = round(float(value), 2)

class Product:
    price = RoundedDescriptor()

if __name__ == "__main__":
    p = Product()
    p.price = 10.55555
    print(p.price) # Вывод: 10.56