import os

# Метод listdir с аргументом "." возвращает всё содержимое текущей папки
files_in_folder = os.listdir(".")
print("Файлы и папки в текущей директории:", files_in_folder)