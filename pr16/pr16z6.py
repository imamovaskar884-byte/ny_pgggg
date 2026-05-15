import re
# Задача 6: Слова на букву a или A
text6 = "Apple and banana are amazing"
print("Задача 6:", re.findall(r'\b[aA]\w*', text6))