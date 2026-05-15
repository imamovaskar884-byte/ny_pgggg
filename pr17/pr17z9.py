from datetime import datetime

# Получаем текущую дату и переводим её в строку нужного формата
# %Y - год, %m - месяц, %d - день
formatted_date = datetime.now().strftime("%Y-%m-%d")
print("Дата в формате YYYY-MM-DD:", formatted_date)