# Задача 16: Преобразовать дату и время в формат "01 January 2024, 14:30"

from datetime import datetime

# Пример с конкретной датой
specific_date = datetime(2024, 1, 1, 14, 30)
formatted = specific_date.strftime("%d %B %Y, %H:%M")
print(f"Пример: {formatted}")

# Или с текущей датой
now = datetime.now()
formatted_now = now.strftime("%d %B %Y, %H:%M")
print(f"Текущая дата: {formatted_now}")