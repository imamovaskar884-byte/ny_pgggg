# Задача 19: Записывать сообщения в файл с текущей датой и временем

from datetime import datetime

message = input("Введите сообщение: ")
now = datetime.now()
formatted = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}"

with open('log_with_time.txt', 'a', encoding='utf-8') as f:
    f.write(formatted + '\n')

print(f"Записано: {formatted}")