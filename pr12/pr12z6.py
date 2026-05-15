def safe_sum(lst):
    total = 0
    for item in lst:
        try:
            total += item
        except TypeError:
            continue
    return total

# Пример
print(safe_sum([1, 2, "a", 3]))  # 6
