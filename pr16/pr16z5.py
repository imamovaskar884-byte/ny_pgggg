import re
# Задача 5: Удаление всех цифр
text5 = "abc123def45"
print("Задача 5:", re.sub(r'\d+', '', text5))