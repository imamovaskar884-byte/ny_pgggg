from datetime import date, timedelta

# Берем текущую дату и прибавляем к ней 7 дней через объект timedelta
future_date = date.today() + timedelta(days=7)
print("Дата через 7 дней:", future_date)