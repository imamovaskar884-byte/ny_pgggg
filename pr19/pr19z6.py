import threading

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

if __name__ == "__main__":
    threads = [threading.Thread(target=increment_safe) for _ in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print(f"Итоговое значение (всегда будет 500000): {counter}")