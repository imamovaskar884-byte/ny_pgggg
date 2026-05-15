def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"

# Пример [cite: 3]
print(safe_divide(10, 2))  # 5.0
print(safe_divide(5, 0))   # Division by zero
