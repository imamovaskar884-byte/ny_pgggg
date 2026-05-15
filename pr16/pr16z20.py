import re
# Задача 20: Анализ текста с логами
text20 = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

# Находим все строки с ERROR и сразу забираем из них даты
error_dates = re.findall(r'^(\d{4}-\d{2}-\d{2})\s+ERROR.*$', text20, re.MULTILINE)

# Считаем количество ошибок по датам
error_counts = {}
for date in error_dates:
    error_counts[date] = error_counts.get(date, 0) + 1

print("Задача 20 - Даты с ошибками:", error_dates)
print("Задача 20 - Количество ошибок по датам:", error_counts)