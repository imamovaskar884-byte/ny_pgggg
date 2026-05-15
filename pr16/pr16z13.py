import re
# Задача 13 (В тексте без номера): Поиск ссылок
text13 = "Go to https://google.com or http://test.org"
print("Задача 13:", re.findall(r'https?://[^\s]+', text13))