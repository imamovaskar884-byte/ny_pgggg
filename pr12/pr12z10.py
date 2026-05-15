def calculator(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            try:
                return a / b
            except ZeroDivisionError:
                return "Division by zero"
        else:
            return "Unknown operation"
    except TypeError:
        return "Type error"

# Пример
print(calculator(5, 3, "+"))   # 8
print(calculator(5, 0, "/"))   # Division by zero
print(calculator(5, 3, "^"))   # Unknown operation
print(calculator(5, "a", "+")) # Type error
