import json

# Открываем файл на чтение ('r') и загружаем данные с помощью load
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    
print("Прочитанное содержимое data.json:")
print(loaded_data)