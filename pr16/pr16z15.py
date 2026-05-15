import re
# Задача 15: Первая буква каждого слова — заглавная
text15 = "hello world python"
print("Задача 15:", re.sub(r'\b\w', lambda m: m.group(0).upper(), text15))