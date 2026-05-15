# 18. Подсчёт ошибок
with open('log.txt', 'r', encoding='utf-8') as f:
    print(sum(1 for line in f if "ERROR" in line))