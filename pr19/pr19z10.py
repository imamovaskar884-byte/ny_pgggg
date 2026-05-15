import threading
import multiprocessing
import time

def heavy_calc():
    return sum(i * i for i in range(10000000))

def run_with_threads():
    threads = [threading.Thread(target=heavy_calc) for _ in range(2)]
    start = time.time()
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Время threading: {time.time() - start:.4f} сек")

def run_with_processes():
    processes = [multiprocessing.Process(target=heavy_calc) for _ in range(2)]
    start = time.time()
    for p in processes: p.start()
    for p in processes: p.join()
    print(f"Время multiprocessing: {time.time() - start:.4f} сек")

if __name__ == "__main__":
    run_with_threads()
    run_with_processes()