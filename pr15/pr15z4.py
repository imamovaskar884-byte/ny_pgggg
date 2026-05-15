# Задача 4: Найти средний возраст из файла data.csv

with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

ages = []

# Пропускаем первую строку (заголовок)
for line in lines[1:]:
    if line.strip():
        name, age = line.strip().split(',')
        ages.append(int(age))

average_age = sum(ages) / len(ages)
print(f"Средний возраст: {average_age:.2f}")