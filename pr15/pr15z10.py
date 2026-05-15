# Задача 10: Записать в новый файл только уникальные строки

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

unique_lines = []
seen = set()

for line in lines:
    stripped = line.rstrip('\n')
    if stripped not in seen:
        seen.add(stripped)
        unique_lines.append(line)

with open('unique.txt', 'w', encoding='utf-8') as out:
    out.writelines(unique_lines)

print("Уникальные строки записаны в unique.txt")