class Adder:
    def add(self, a, b=None):
        if b is None:
            return a + 10
        return a + b

# Проверка
a = Adder()
print(a.add(5))     # 15
print(a.add(3, 4))  # 7
