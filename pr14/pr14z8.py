def average(*args: float) -> float:
    if not args:
        return 0.0
    return sum(args) / len(args)

# Пример использования 
print(average(2, 4, 6))  # Вывод: 4.0
