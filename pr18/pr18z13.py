# 13. Нумерация строк
with open('input.txt', 'r', encoding='utf-8') as fin, open('numbered.txt', 'w', encoding='utf-8') as fout:
    for i, line in enumerate(fin, 1):
        fout.write(f"{i}: {line}")