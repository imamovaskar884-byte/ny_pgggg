# Задача 2: Посчитать частоту каждого слова в файле input.txt

from collections import Counter
import string

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Разбиваем на слова
words = text.split()

# Очищаем от знаков препинания
words = [word.strip(string.punctuation) for word in words]

# Приводим к нижнему регистру и убираем пустые
words = [word.lower() for word in words if word]

# Считаем частоту
counter = Counter(words)

# Выводим, сортируя по убыванию частоты
for word, count in counter.most_common():
    print(f"{word}: {count}")