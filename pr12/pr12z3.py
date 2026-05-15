def safe_operation(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

# Пример
print(safe_operation(10, 2))   # 5.0
print(safe_operation(5, 0))    # Division by zero
print(safe_operation(5, "a"))  # Type error
