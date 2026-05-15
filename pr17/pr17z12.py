import os

file_name = "data.txt"
# Проверяем, существует ли файл по указанному пути
is_exist = os.path.exists(file_name)
print(f"Существует ли файл {file_name}? {is_exist}")