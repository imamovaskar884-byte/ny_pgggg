import multiprocessing
import math

def calculate_factorials(start_num, end_num):
    for i in range(start_num, end_num):
        math.factorial(i)
    print(f"Процесс завершил вычисления от {start_num} до {end_num}")

if __name__ == "__main__":
    ranges = [(1, 5000), (5000, 10000), (10000, 15000), (15000, 20000)]
    processes = []
    
    for start, end in ranges:
        p = multiprocessing.Process(target=calculate_factorials, args=(start, end))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()