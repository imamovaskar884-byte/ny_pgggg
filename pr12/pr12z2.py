def to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Invalid input"

# Пример
print(to_int("123"))  # 123
print(to_int("abc"))  # Invalid input
