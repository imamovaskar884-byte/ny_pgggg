import threading
import time

def print_numbers(thread_name):
    for i in range(1, 6):
        print(f"{thread_name}: {i}")
        time.sleep(0.1)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers, args=("Поток-1",))
    t2 = threading.Thread(target=print_numbers, args=("Поток-2",))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()