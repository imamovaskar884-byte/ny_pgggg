import threading
import time

def download_file(filename):
    print(f"Начало загрузки файла {filename}...")
    time.sleep(2) # Имитация сетевой задержки
    print(f"Файл {filename} успешно загружен!")

if __name__ == "__main__":
    files = ["document.pdf", "image.png", "archive.zip"]
    threads = []
    
    start_time = time.time()
    
    for f in files:
        t = threading.Thread(target=download_file, args=(f,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Все файлы загружены за {time.time() - start_time:.2f} сек.")