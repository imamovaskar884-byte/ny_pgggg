# 10. Чтение и запись одновременно (в верхнем регистре)
with open('input.txt', 'r', encoding='utf-8') as fin, open('upper.txt', 'w', encoding='utf-8') as fout:
    fout.write(fin.read().upper())