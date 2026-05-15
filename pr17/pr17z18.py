import csv

# Открываем файл и читаем его построчно с помощью цикла
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("Содержимое CSV-файла:")
    for row in reader:
        print(row)