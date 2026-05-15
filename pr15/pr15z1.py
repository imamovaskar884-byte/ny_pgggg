# Задача 1: Найти количество уникальных слов в файле input.txt

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Разбиваем на слова
words = text.split()

# Очищаем от знаков препинания
import string
words = [word.strip(string.punctuation) for word in words]

# Приводим к нижнему регистру и убираем пустые
words = [word.lower() for word in words if word]

# Находим уникальные слова
unique_words = set(words)

print(f"Количество уникальных слов: {len(unique_words)}")