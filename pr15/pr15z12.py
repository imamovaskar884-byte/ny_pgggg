# Задача 12: Посчитать количество рабочих дней между двумя датами

from datetime import datetime, timedelta

start_str = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
end_str = input("Введите конечную дату (ГГГГ-ММ-ДД): ")

start = datetime.strptime(start_str, "%Y-%m-%d").date()
end = datetime.strptime(end_str, "%Y-%m-%d").date()

workdays = 0
current = start

while current <= end:
    if current.weekday() < 5:  # 0-пн, 4-пт, 5-сб, 6-вс
        workdays += 1
    current += timedelta(days=1)

print(f"Количество рабочих дней (пн-пт): {workdays}")