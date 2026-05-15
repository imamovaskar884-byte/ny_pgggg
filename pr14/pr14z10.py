def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    # Складываем a, b, сумму args и сумму значений kwargs
    return a + b + sum(args) + sum(kwargs.values())

# Пример использования
print(process(1, 2, 3, 4, x=5, y=6))  # Вывод: 21

