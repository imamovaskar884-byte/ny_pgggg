# 12. Фильтрация строк (> 5 символов)
with open('input.txt', 'r', encoding='utf-8') as fin, open('filtered.txt', 'w', encoding='utf-8') as fout:
    fout.writelines(line for line in fin if len(line.strip()) > 5)