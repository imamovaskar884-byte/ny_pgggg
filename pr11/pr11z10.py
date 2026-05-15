def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x * x
        return x + y

class AdvancedCalculator(Calculator):
    def calculate(self, x, y=None):
        # Вызываем метод родителя и прибавляем 10
        result = super().calculate(x, y)
        return result + 10

# Проверка
calc = AdvancedCalculator()
# Вручную оборачиваем метод в декоратор согласно примеру в задании
calc.calculate = log_call(calc.calculate)

print(calc.calculate(5))    # (5*5) + 10 = 35
print(calc.calculate(2, 3)) # (2+3) + 10 = 15
