# 1. Чтение файла через with
with open('input.txt', 'r', encoding='utf-8') as f:
    print(f.read())