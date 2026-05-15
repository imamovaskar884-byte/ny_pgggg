def read_number(s):
    try:
        result = int(s)
        return result
    except (ValueError, TypeError):
        return "Error"
    finally:
        print("Done")

# Пример
print(read_number("10"))
print(read_number("abc"))
