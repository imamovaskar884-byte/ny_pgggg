import re
# Задача 4: Замена пробелов на '_'
text4 = "Hello world Python"
print("Задача 4:", re.sub(r'\s+', '_', text4))