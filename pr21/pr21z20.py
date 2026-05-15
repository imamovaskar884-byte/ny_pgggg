class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, value):
        self.grades.append(value)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

s1 = Student("Игорь", 19)
s1.add_grade(4)
s1.add_grade(5)
s1.add_grade(4)

s2 = Student("Ольга", 20)
s2.add_grade(5)
s2.add_grade(5)

print(f"Студент {s1.name}, средний балл: {s1.average():.2f}")
print(f"Студент {s2.name}, средний балл: {s2.average():.2f}")

try:
    s1.course = 2
except AttributeError:
    print("Проверка: Нельзя добавить новый атрибут (course).")

