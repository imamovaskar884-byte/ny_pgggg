# Задача 3: Удалить знаки препинания и записать в clean.txt

import string

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Удаляем знаки препинания
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)

# Записываем результат
with open('clean.txt', 'w', encoding='utf-8') as f:
    f.write(clean_text)

print("Результат записан в clean.txt")