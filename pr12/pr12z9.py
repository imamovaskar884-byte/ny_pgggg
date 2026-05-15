def safe_print_number(s):
    try:
        num = int(s)
    except ValueError:
        print("Error")
    else:
        print(num)

# Пример
safe_print_number("5")    # 5
safe_print_number("abc")  # Error
