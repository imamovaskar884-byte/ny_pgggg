# Задача 13: Найти ближайший следующий понедельник

from datetime import datetime, timedelta

date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

# days_until_monday = (7 - текущий_день_недели) % 7
days_until_monday = (7 - date_obj.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7  # следующий понедельник, а не сегодня

next_monday = date_obj + timedelta(days=days_until_monday)
print(f"Ближайший следующий понедельник: {next_monday}")