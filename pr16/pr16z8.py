import re
# Задача 8: Поиск дат YYYY-MM-DD
text8 = "Dates: 2024-01-01 and 2025-12-31"
print("Задача 8:", re.findall(r'\d{4}-\d{2}-\d{2}', text8))