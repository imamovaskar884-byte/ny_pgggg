# 5. Подсчёт строк
with open('input.txt', 'r', encoding='utf-8') as f:
    print(sum(1 for _ in f))