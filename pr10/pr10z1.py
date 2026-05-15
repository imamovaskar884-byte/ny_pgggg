class NumberWrapper:
    """Класс для демонстрации переопределения оператора сложения '+'."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __add__(self, other):
        """Переопределяет оператор сложения '+'."""
        if isinstance(other, NumberWrapper):
            return NumberWrapper(self.value + other.value)
        elif isinstance(other, (int, float)):
            return NumberWrapper(self.value + other)
        else:
            return NotImplemented # Указывает, что операция не поддерживается для данного типа

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"NumberWrapper({self.value})"

# --- Пример использования ---
num1 = NumberWrapper(10)
num2 = NumberWrapper(5)
sum_result = num1 + num2
print(f"1. Сложение: {num1} + {num2} = {sum_result}")

num3 = NumberWrapper(20)
sum_with_int = num3 + 7
print(f"1. Сложение с числом: {num3} + 7 = {sum_with_int}")

