class NumberWrapperSub:
    """Класс для демонстрации переопределения оператора вычитания '-'."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __sub__(self, other):
        """Переопределяет оператор вычитания '-'."""
        if isinstance(other, NumberWrapperSub):
            return NumberWrapperSub(self.value - other.value)
        elif isinstance(other, (int, float)):
            return NumberWrapperSub(self.value - other)
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"NumberWrapperSub({self.value})"

# --- Пример использования ---
sub1 = NumberWrapperSub(15)
sub2 = NumberWrapperSub(8)
diff_result = sub1 - sub2
print(f"2. Вычитание: {sub1} - {sub2} = {diff_result}")

sub3 = NumberWrapperSub(30)
diff_with_int = sub3 - 12
print(f"2. Вычитание с числом: {sub3} - 12 = {diff_with_int}")
