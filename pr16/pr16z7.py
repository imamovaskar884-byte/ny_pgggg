import re
# Задача 7: Проверка номера формата +371XXXXXXXX
text7 = "+37112345678"
print("Задача 7:", bool(re.fullmatch(r'\+371\d{8}', text7)))