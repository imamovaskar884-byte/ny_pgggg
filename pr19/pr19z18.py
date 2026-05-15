import asyncio
import random

async def read_file(filename):
    print(f"Открываем файл {filename}...")
    read_time = random.uniform(0.5, 2.5)
    await asyncio.sleep(read_time)
    print(f"Файл {filename} прочитан за {read_time:.2f} сек.")

async def main():
    files_to_read = ["data.csv", "config.json", "log.txt"]
    tasks = [read_file(f) for f in files_to_read]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())