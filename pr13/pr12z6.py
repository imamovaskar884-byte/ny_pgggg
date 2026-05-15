class Validator:
    @staticmethod
    def is_positive(n):
        return n > 0

print(Validator.is_positive(5))   # Вывод: True
print(Validator.is_positive(-3))  # Вывод: False

