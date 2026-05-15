import re
# Задача 2: Поиск всех чисел
text2 = "There are 12 apples and 5 bananas"
print("Задача 2:", re.findall(r'\d+', text2))