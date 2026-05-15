# 14. Удаление пустых строк
with open('input.txt', 'r', encoding='utf-8') as fin, open('no_empty.txt', 'w', encoding='utf-8') as fout:
    fout.writelines(line for line in fin if line.strip())