# Задача 18: Определить, просрочен ли дедлайн

from datetime import datetime

deadline_str = input("Введите дату дедлайна (ГГГГ-ММ-ДД): ")
deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
today = datetime.now().date()

if deadline < today:
    print("Дедлайн ПРОСРОЧЕН!")
elif deadline == today:
    print("Дедлайн СЕГОДНЯ!")
else:
    days_left = (deadline - today).days
    print(f"Дедлайн ещё не наступил. Осталось {days_left} дней")