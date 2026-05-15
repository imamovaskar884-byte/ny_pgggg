# Задача 7: Найти и вывести все строки, содержащие "ERROR"

with open('log.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Строки с ошибками (ERROR):")
for line in lines:
    if "ERROR" in line:
        print(line.strip())