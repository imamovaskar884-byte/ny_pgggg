# Задача 6: Найти самую длинную строку в файле

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

longest_line = ""
max_length = 0

for line in lines:
    line_stripped = line.rstrip('\n')
    if len(line_stripped) > max_length:
        max_length = len(line_stripped)
        longest_line = line_stripped

print(f"Длина самой длинной строки: {max_length}")
print(f"Самая длинная строка: {longest_line}")