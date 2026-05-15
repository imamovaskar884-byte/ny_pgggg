class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return f"({self.x}, {self.y})"

p = Point(10, 15)
print(f"Координаты: {p.get_coordinates()}")
