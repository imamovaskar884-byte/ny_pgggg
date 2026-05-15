class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

class Programmer(Worker):
    def work(self):
        print("Coding...")

# Проверка
staff = [Worker(), Teacher(), Programmer()]
for person in staff:
    person.work()
