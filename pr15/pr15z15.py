# Задача 15: Отсортировать список дат по возрастанию

from datetime import datetime

dates_str = [
    "2024-12-31",
    "2023-01-15",
    "2024-06-01",
    "2023-12-25",
    "2025-01-01"
]

print("Исходные даты:")
for d in dates_str:
    print(d)

# Преобразуем в объекты дат и сортируем
dates_obj = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]
dates_obj.sort()

# Преобразуем обратно в строки
sorted_dates = [d.strftime("%Y-%m-%d") for d in dates_obj]

print("\nОтсортированные даты:")
for d in sorted_dates:
    print(d)