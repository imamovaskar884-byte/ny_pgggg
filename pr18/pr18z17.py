# 17. Чтение логов (только ERROR)
with open('log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())