# Задача 20: Найти ошибки из log.txt и посчитать их по дням

from collections import defaultdict

error_by_day = defaultdict(int)

try:
    with open('log.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if "ERROR" in line:
                # Извлекаем дату (первые 10 символов, если формат ГГГГ-ММ-ДД)
                date_str = line[:10]
                error_by_day[date_str] += 1
    
    print("Количество ошибок по дням:")
    for date, count in sorted(error_by_day.items()):
        print(f"{date}: {count}")
        
    if not error_by_day:
        print("Ошибок (ERROR) не найдено")
        
except FileNotFoundError:
    print("Файл log.txt не найден!")