import asyncio
import random

async def task_worker(name, queue):
    while True:
        task_id = await queue.get()
        print(f"[{name}] Взял в работу задачу #{task_id}")
        
        # Каждая задача выполняется с задержкой
        execution_time = random.uniform(0.5, 1.5)
        await asyncio.sleep(execution_time)
        
        print(f"[{name}] Успешно завершил задачу #{task_id}")
        queue.task_done()

async def main():
    task_queue = asyncio.Queue()
    
    # Добавляем 10 задач в очередь
    for i in range(1, 11):
        await task_queue.put(i)
        
    # Создаем 3 worker'ов
    workers = [asyncio.create_task(task_worker(f"Worker-{i}", task_queue)) for i in range(1, 4)]
    
    # Ждем, пока все задачи из очереди не будут выполнены
    await task_queue.join()
    print("Все задачи обработаны!")
    
    # Останавливаем worker'ов
    for w in workers:
        w.cancel()

if __name__ == "__main__":
    asyncio.run(main())