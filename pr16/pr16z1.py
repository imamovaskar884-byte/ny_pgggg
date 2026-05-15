import re

# Задача 1: Проверка на наличие слова "Python"
text1 = "I love Python programming"
print("Задача 1:", bool(re.search(r'\bPython\b', text1)))
