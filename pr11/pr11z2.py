class Multiplier:
    def multiply(self, a, b=None):
        if b is None:
            return a * a
        return a * b

# Проверка
m = Multiplier()
print(m.multiply(5))     # 25
print(m.multiply(2, 3))  # 6
