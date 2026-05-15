import asyncio

async def task_with_delay(task_id, delay):
    await asyncio.sleep(delay)
    print(f"Задача {task_id} завершена. Время ожидания: {delay}с.")

async def main():
    delays = [2.0, 0.5, 1.5, 3.0, 1.0]
    tasks = [task_with_delay(i+1, delays[i]) for i in range(5)]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())