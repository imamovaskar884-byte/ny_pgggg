# 6. Подсчёт слов
with open('input.txt', 'r', encoding='utf-8') as f:
    print(len(f.read().split()))