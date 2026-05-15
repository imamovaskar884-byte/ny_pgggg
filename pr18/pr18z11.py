# 11. Контекстный менеджер с несколькими файлами
with open('input.txt', 'r', encoding='utf-8') as fin, open('output.txt', 'w', encoding='utf-8') as fout:
    fout.write(fin.read())