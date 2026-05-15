import asyncio

async def print_message(msg):
    await asyncio.sleep(1)
    print(msg)

async def main():
    task1 = asyncio.create_task(print_message("Первая задача"))
    task2 = asyncio.create_task(print_message("Вторая задача"))
    task3 = asyncio.create_task(print_message("Третья задача"))
    
    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(main())