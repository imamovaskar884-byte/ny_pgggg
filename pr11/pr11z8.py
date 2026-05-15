def check_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
            print("Error")
            return
        return func(*args, **kwargs)
    return wrapper	

@check_positive
def multiply(a, b):
    print(a * b)

# Проверка
multiply(3, 4)   # 12
multiply(3, -1)  # Error
