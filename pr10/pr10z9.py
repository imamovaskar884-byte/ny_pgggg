class Counter:
    """Класс для демонстрации переопределения оператора '+='."""

    def __init__(self, count=0):
        if not isinstance(count, int):
            raise TypeError("Значение счетчика должно быть целым числом.")
        self.count = count

    def __iadd__(self, other):
        """Переопределяет оператор '+=' (инкремент)."""
        if isinstance(other, int):
            self.count += other
            return self # Важно вернуть self для работы in-place
        else:
            return NotImplemented

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Counter({self.count})"

# --- Пример использования ---
my_counter = Counter(10)
print(f"9. Начальное значение: {my_counter}")

my_counter += 5 # Это вызовет my_counter.__iadd__(5)
print(f"9. После my_counter += 5: {my_counter}")

my_counter += 2
print(f"9. После my_counter += 2: {my_counter}")

