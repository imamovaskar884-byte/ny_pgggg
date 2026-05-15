import threading

def print_name(name):
    for _ in range(5):
        print(f"Меня зовут {name}")

if __name__ == "__main__":
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=print_name, args=(f"Thread-{i}",))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()