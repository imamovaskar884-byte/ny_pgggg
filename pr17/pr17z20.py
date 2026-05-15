import random
import os
from datetime import datetime

file_name = "numbers.txt"

# 1. Генерируем список из 5 случайных чисел от 1 до 100
random_nums = [random.randint(1, 100) for _ in range(5)]

# 2. Сохраняем числа и текущую дату в файл
with open(file_name, "w", encoding="utf-8") as file:
    current_time = datetime.now()
    file.write(f"Дата и время записи: {current_time}\n")
    file.write(f"Случайные числа: {random_nums}\n")

# 3. Проверяем, существует ли файл
if os.path.exists(file_name):
    print("Файл numbers.txt успешно найден!\n")
    
    # 4. Читаем файл и выводим его содержимое в консоль
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
else:
    print("Произошла ошибка, файл не найден.")