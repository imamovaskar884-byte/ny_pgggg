def multiply_all(*args: int) -> int:
    result = 1
    for num in args:
        result *= num
    return result

# Пример использования 
print(multiply_all(2, 3, 4))  # Вывод: 24
