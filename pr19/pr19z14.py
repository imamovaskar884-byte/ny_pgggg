import asyncio

async def my_async_function():
    print("Начало асинхронной функции...")
    await asyncio.sleep(1)
    print("Конец асинхронной функции!")

if __name__ == "__main__":
    asyncio.run(my_async_function())