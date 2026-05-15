import threading
import queue
import time

def producer(q):
    for i in range(1, 6):
        print(f"[Producer] Кладу в очередь элемент {i}")
        q.put(i)
        time.sleep(0.5)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"[Consumer] Достал из очереди элемент {item}")
        q.task_done()

if __name__ == "__main__":
    q = queue.Queue()
    
    t_producer = threading.Thread(target=producer, args=(q,))
    t_consumer = threading.Thread(target=consumer, args=(q,))
    
    t_producer.start()
    t_consumer.start()
    
    t_producer.join()
    q.put(None) # Сигнал консьюмеру об остановке
    t_consumer.join()