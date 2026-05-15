# 8. Проверка пустого файла
import os
if os.path.exists('input.txt') and os.stat('input.txt').st_size == 0:
    print("Empty")