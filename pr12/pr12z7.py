def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index error"

# Пример
print(get_element([1, 2, 3], 1))  # 2
print(get_element([1, 2, 3], 5))  # Index error
