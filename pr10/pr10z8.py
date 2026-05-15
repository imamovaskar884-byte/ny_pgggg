class BooleanWrapper:
    """Класс для демонстрации переопределения __bool__."""

    def __init__(self, value):
        if not isinstance(value, bool):
            raise TypeError("Значение должно быть булевым (True или False).")
        self.value = value

    def __bool__(self):
        """Переопределяет поведение объекта в булевом контексте."""
        return self.value

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"BooleanWrapper({self.value})"

# --- Пример использования ---
bool_true = BooleanWrapper(True)
bool_false = BooleanWrapper(False)

print(f"8. Булево представление (True): {bool_true} -> {bool(bool_true)}")
print(f"8. Булево представление (False): {bool_false} -> {bool(bool_false)}")

# Применение оператора 'not'
print(f"8. not {bool_true} = {not bool_true}")
print(f"8. not {bool_false} = {not bool_false}")
