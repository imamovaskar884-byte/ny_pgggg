import asyncio

async def worker(number):
    await asyncio.sleep(1)
    return f"Результат от воркера {number}"

async def main():
    results = await asyncio.gather(
        worker(1),
        worker(2),
        worker(3)
    )
    print("Все задачи завершены. Результаты:")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())