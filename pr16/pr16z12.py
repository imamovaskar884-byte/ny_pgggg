import re
# Задача 12: Удаление HTML-тегов
text12 = "<p>Hello</p>"
print("Задача 12:", re.sub(r'<[^>]+>', '', text12))
