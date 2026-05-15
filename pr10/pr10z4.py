class Divider:
    """Класс для демонстрации переопределения оператора деления '/'."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __truediv__(self, other):
        """Переопределяет оператор деления '/'."""
        if isinstance(other, Divider):
            if other.value == 0:
                raise ZeroDivisionError("Деление на ноль.")
            return Divider(self.value / other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль.")
            return Divider(self.value / other)
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Divider({self.value})"

# --- Пример использования ---
div1 = Divider(20)
div2 = Divider(4)
quot_result = div1 / div2
print(f"4. Деление: {div1} / {div2} = {quot_result}")

div3 = Divider(50)
quot_with_int = div3 / 5
print(f"4. Деление с числом: {div3} / 5 = {quot_with_int}")
