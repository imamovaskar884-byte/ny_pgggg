import re
# Задача 3: Проверка корректности email
text3 = "test@example.com"
print("Задача 3:", bool(re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', text3)))