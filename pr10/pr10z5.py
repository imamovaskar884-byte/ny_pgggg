class ComparableNumber:
    """Класс для демонстрации переопределения оператора '<'."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __lt__(self, other):
        """Переопределяет оператор '<'."""
        if isinstance(other, ComparableNumber):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"ComparableNumber({self.value})"

# --- Пример использования ---
comp1 = ComparableNumber(7)
comp2 = ComparableNumber(12)
print(f"5. Сравнение '<': {comp1} < {comp2} = {comp1 < comp2}")

comp3 = ComparableNumber(15)
print(f"5. Сравнение '<' с числом: {comp3} < 20 = {comp3 < 20}")
