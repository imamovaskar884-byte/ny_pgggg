import json

my_dict = {"name": "Ivan", "age": 20, "city": "Kazan"}

# Открываем файл на запись ('w') и сохраняем словарь туда с помощью dump
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(my_dict, file, ensure_ascii=False, indent=4)
print("Данные успешно сохранены в data.json")