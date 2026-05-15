import asyncio

async def producer(queue):
    for i in range(1, 4):
        item = f"Сообщение-{i}"
        print(f"[Producer] Отправляет: {item}")
        await queue.put(item)
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"[Consumer] Получил и обрабатывает: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    q = asyncio.Queue()
    
    prod = asyncio.create_task(producer(q))
    cons = asyncio.create_task(consumer(q))
    
    await prod
    await q.join()
    cons.cancel()

if __name__ == "__main__":
    asyncio.run(main())