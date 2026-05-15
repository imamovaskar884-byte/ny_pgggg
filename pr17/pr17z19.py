import random
from datetime import date, timedelta

# Задаем начальную дату (1 января 2024)
start_date = date(2024, 1, 1)

# В 2024 году 366 дней. Генерируем случайный сдвиг от 0 до 365
random_days_to_add = random.randint(0, 365)

# Прибавляем случайное число дней к 1 января
random_date_2024 = start_date + timedelta(days=random_days_to_add)
print("Случайная дата в 2024 году:", random_date_2024)