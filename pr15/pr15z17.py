# Задача 17: Преобразовать текущую дату в UNIX timestamp и обратно

from datetime import datetime

# Текущее время
now = datetime.now()
timestamp = int(now.timestamp())
print(f"Текущая дата: {now}")
print(f"UNIX timestamp: {timestamp}")

# Обратно в datetime
from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Из timestamp обратно: {from_timestamp}")