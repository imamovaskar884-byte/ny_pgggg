import re
# Задача 10: Разделение строки по запятым и пробелам
text10 = "apple, banana orange,grape"
print("Задача 10:", [word for word in re.split(r'[,\s]+', text10) if word])