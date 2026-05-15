import re
# Задача 19: Извлечение имени и возраста
text19 = "Name: John Age: 25"
match19 = re.search(r'Name:\s*(\w+)\s*Age:\s*(\d+)', text19)
if match19:
    print("Задача 19:", match19.groups())