class Vector2D:
    """Класс для представления двумерных векторов с переопределением операторов."""

    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Компоненты вектора должны быть числами.")
        self.x = x
        self.y = y

    def __add__(self, other):
        """Переопределяет оператор сложения '+' для векторов."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        """Переопределяет оператор вычитания '-' для векторов."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление вектора."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Возвращает 'официальное' строковое представление объекта."""
        return f"Vector2D(x={self.x}, y={self.y})"

# --- Пример использования ---
v1 = Vector2D(3, 5)
v2 = Vector2D(1, 2)

# Сложение
sum_vec = v1 + v2
print(f"10. Сложение векторов: {v1} + {v2} = {sum_vec}")

# Вычитание
diff_vec = v1 - v2
print(f"10. Вычитание векторов: {v1} - {v2} = {diff_vec}")

# Совместное использование
v3 = Vector2D(10, 20)
result_complex = (v1 + v2) - Vector2D(1, 1)
print(f"10. Комплексная операция: ({v1} + {v2}) - (1, 1) = {result_complex}")
