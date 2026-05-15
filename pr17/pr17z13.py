import os

file_name = "data.txt"

# Создадим пустой файл для теста, если его нет
if not os.path.exists(file_name):
    open(file_name, "w").close()

# Получаем размер файла в байтах
file_size = os.path.getsize(file_name)
print(f"Размер файла {file_name} в байтах:", file_size)