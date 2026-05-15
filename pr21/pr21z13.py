class Person:
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

class Student(Person):
    __slots__ = ('grade',)

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Мария", 5)
print(f"Студент: {s.name}, Оценка: {s.grade}")
