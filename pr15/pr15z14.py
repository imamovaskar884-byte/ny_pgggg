# Задача 14: Вычислить возраст в днях

from datetime import datetime

birth_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
birth = datetime.strptime(birth_str, "%Y-%m-%d").date()
today = datetime.now().date()

age_days = (today - birth).days
print(f"Ваш возраст в днях: {age_days}")