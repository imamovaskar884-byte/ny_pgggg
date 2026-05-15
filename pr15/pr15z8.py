# Задача 8: Посчитать строки, начинающиеся с заглавной буквы

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for line in lines:
    stripped = line.strip()
    if stripped and stripped[0].isupper():
        count += 1

print(f"Строк, начинающихся с заглавной буквы: {count}")