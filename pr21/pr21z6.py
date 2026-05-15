class Student:
    __slots__ = ('name', 'grade')

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        self.grade = new_grade
        print(f"Оценка студента {self.name} изменена на {self.grade}")

s = Student("Анна", 4)
s.change_grade(5)
