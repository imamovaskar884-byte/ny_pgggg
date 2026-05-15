import threading
import queue
import time

def worker(q, worker_id):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Worker {worker_id} начал обработку задачи: {item}")
        time.sleep(1)
        print(f"Worker {worker_id} закончил задачу: {item}")
        q.task_done()

if __name__ == "__main__":
    task_queue = queue.Queue()
    workers = []
    
    # Создаем 3 worker-потока
    for i in range(3):
        t = threading.Thread(target=worker, args=(task_queue, i))
        t.start()
        workers.append(t)
        
    # Добавляем 10 задач
    for item in range(1, 11):
        task_queue.put(f"Task-{item}")
        
    task_queue.join() # Ждем завершения всех задач
    
    for _ in range(3):
        task_queue.put(None) # Останавливаем потоки
    for t in workers:
        t.join()