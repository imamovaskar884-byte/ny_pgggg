import threading
import time

def print_name_with_delay(name):
    for _ in range(5):
        print(f"Меня зовут {name}")
        time.sleep(1)

if __name__ == "__main__":
    threads = [threading.Thread(target=print_name_with_delay, args=(f"Thread-{i}",)) for i in range(1, 4)]
    
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()