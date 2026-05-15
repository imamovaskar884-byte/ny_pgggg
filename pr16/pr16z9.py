import re
# Задача 9: Проверка пароля (минимум 8 символов, хотя бы 1 цифра)
text9 = "MyPass123"
print("Задача 9:", bool(re.fullmatch(r'(?=.*\d).{8,}', text9)))