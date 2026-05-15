# Задача 5: Записать в новый файл строки, где возраст больше 25

with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('filtered.csv', 'w', encoding='utf-8') as out:
    # Записываем заголовок
    out.write(lines[0])
    
    # Проверяем каждую строку
    for line in lines[1:]:
        if line.strip():
            name, age = line.strip().split(',')
            if int(age) > 25:
                out.write(line)

print("Отфильтрованные данные записаны в filtered.csv")