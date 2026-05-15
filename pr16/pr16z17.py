import re
# Задача 17: Извлечение даты, уровня и сообщения из лога
text17 = "2026-04-15 INFO Everything is fine"
match17 = re.search(r'(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.*)', text17)
if match17:
    print("Задача 17:", match17.groups())