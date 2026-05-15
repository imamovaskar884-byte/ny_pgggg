class EqualNumber:
    """Класс для демонстрации переопределения оператора '=='."""

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def __eq__(self, other):
        """Переопределяет оператор '=='."""
        if isinstance(other, EqualNumber):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"EqualNumber({self.value})"

# --- Пример использования ---
eq1 = EqualNumber(10)
eq2 = EqualNumber(10)
eq3 = EqualNumber(5)
print(f"6. Сравнение '==': {eq1} == {eq2} = {eq1 == eq2}")
print(f"6. Сравнение '==': {eq1} == {eq3} = {eq1 == eq3}")

eq4 = EqualNumber(15)
print(f"6. Сравнение '==' с числом: {eq4} == 15 = {eq4 == 15}")

            

Задача 7: Переопределение метода строкового представления (__str__)

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

