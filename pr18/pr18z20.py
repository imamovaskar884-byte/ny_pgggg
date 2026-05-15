# 20. Безопасная работа с файлом
class SafeFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        except Exception as e:
            print(f"Ошибка чтения: {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("File closed")
        return True # Подавление исключений

with SafeFileManager('input.txt', 'r') as f:
    if f:
        f.read()