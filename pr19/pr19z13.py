import threading
import time

def background_task():
    while True:
        print("[Daemon] Произвожу фоновую работу...")
        time.sleep(1)

if __name__ == "__main__":
    daemon_thread = threading.Thread(target=background_task, daemon=True)
    daemon_thread.start()
    
    print("Основной поток делает свои дела...")
    time.sleep(3.5)
    print("Основной поток завершает работу. Демон будет остановлен автоматически.")