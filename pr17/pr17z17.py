import csv

users_data = [
    ["Имя", "Возраст"],
    ["Алексей", 22],
    ["Мария", 21]
]

# Создаем csv файл. newline="" нужен, чтобы не было лишних пустых строк
with open("users.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users_data)  # Записываем все строки сразу
print("CSV-файл создан и заполнен")