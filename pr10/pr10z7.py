class Person:
    """Класс для демонстрации переопределения __str__."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Возвращает удобочитаемое строковое представление объекта."""
        return f"Человек: {self.name}, Возраст: {self.age} лет."

    def __repr__(self):
        """Возвращает 'официальное' строковое представление объекта."""
        return f"Person(name='{self.name}', age={self.age})"

# --- Пример использования ---
person1 = Person("Иван", 30)
print(f"7. Строковое представление: {person1}")
print(f"7. Представление для отладки (repr): {repr(person1)}")
