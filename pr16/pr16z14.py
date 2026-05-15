import re
# Задача 14: Поиск повторяющихся подряд слов
text14 = "hello hello world"
print("Задача 14:", re.findall(r'\b(\w+)\s+\1\b', text14))