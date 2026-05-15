class Multiplier:
    """Класс для демонстрации переопределения оператора умножения '*'."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __mul__(self, other):
        """Переопределяет оператор умножения '*'."""
        if isinstance(other, Multiplier):
            return Multiplier(self.value * other.value)
        elif isinstance(other, (int, float)):
            return Multiplier(self.value * other)
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Multiplier({self.value})"

# --- Пример использования ---
mul1 = Multiplier(6)
mul2 = Multiplier(3)
prod_result = mul1 * mul2
print(f"3. Умножение: {mul1} * {mul2} = {prod_result}")

mul3 = Multiplier(5)
prod_with_int = mul3 * 4
print(f"3. Умножение с числом: {mul3} * 4 = {prod_with_int}")
