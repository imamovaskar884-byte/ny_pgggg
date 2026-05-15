def process_data(a, b):
    try:
        val_a = float(a)
        val_b = float(b)
        try:
            return val_a / val_b
        except ZeroDivisionError:
            return "Division by zero"
    except (ValueError, TypeError):
        return "Conversion error"

# Пример
print(process_data("10", "2"))  # 5.0
print(process_data("10", "0"))  # Division by zero
print(process_data("a", "2"))   # Conversion error
