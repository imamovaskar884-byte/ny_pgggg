# Задача 11: Преобразовать строку в объект даты

from datetime import datetime

date_str = "2024-12-31"
date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

print(f"Дата: {date_obj}")
print(f"Год: {date_obj.year}")
print(f"Месяц: {date_obj.month}")
print(f"День: {date_obj.day}")