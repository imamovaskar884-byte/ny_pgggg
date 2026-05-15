class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Если значение еще не вычислялось
        if self.name not in instance.__dict__:
            print(f"Вычисление {self.name}...")
            instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]

class MathOps:
    @CachedProperty
    def heavy_calc(self):
        # Имитация тяжелых вычислений
        return sum(range(1000000))

if __name__ == "__main__":
    m = MathOps()
    print(m.heavy_calc) 
    print(m.heavy_calc) 