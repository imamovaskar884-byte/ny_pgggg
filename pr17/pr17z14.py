import os

folder_name = "folder"
file_name = "file.txt"

# Метод join безопасно склеивает пути (добавляет нужные слеши: / или \)
full_path = os.path.join(folder_name, file_name)
print("Объединенный путь:", full_path)