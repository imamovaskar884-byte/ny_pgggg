def excited(func):
    def wrapper(*args, **kwargs):
        print("Let's go!")
        return func(*args, **kwargs)
    return wrapper

class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

# Проверка
t = Teacher()
t.work = excited(t.work)
t.work()
