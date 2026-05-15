# 7. Копирование файла
with open('input.txt', 'r', encoding='utf-8') as fin, open('copy.txt', 'w', encoding='utf-8') as fout:
    fout.write(fin.read())