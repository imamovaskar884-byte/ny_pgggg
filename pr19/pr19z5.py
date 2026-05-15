import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1 # Потенциальное место для гонки данных

if __name__ == "__main__":
    threads = [threading.Thread(target=increment) for _ in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print(f"Итоговое значение (ожидалось 500000): {counter}")