class ObjectCounterDescriptor:
    def __init__(self):
        self.instances = set()

    def __get__(self, instance, owner):
        if instance is not None:
            self.instances.add(id(instance))
        return len(self.instances)

class TrackedClass:
    counter = ObjectCounterDescriptor()

if __name__ == "__main__":
    obj1 = TrackedClass()
    obj2 = TrackedClass()
    
    print(obj1.counter) # Зарегистрирует obj1, Вывод: 1
    print(obj2.counter) # Зарегистрирует obj2, Вывод: 2
    print(TrackedClass.counter) # Вывод: 2