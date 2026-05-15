class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1.add(v2)
print(f"Результат сложения: ({v3.x}, {v3.y})")
