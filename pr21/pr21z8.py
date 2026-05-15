class Rectangle:
    __slots__ = ('width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print(f"Площадь прямоугольника: {r.area()}")
