class Employee:
    __slots__ = ('name', 'salary')

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

emp = Employee("Алексей", 50000)
emp.increase_salary(10)
print(f"Новая зарплата {emp.name}: {emp.salary:.2f}")
