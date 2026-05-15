# Задача 9: Объединить file1.txt и file2.txt в result.txt

files = ['file1.txt', 'file2.txt']

with open('result.txt', 'w', encoding='utf-8') as out:
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as infile:
                out.write(infile.read())
                out.write('\n')  # Разделитель между файлами
            print(f"Добавлен файл: {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден, пропускаем")

print("Файлы объединены в result.txt")