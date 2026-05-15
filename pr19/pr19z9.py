import multiprocessing

def calc_sum(process_name):
    total = sum(range(1, 100001))
    print(f"[{process_name}] Сумма: {total}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calc_sum, args=("Процесс-1",))
    p2 = multiprocessing.Process(target=calc_sum, args=("Процесс-2",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()