from shape import Shape
import math

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius:.2f}"

    @classmethod
    def get_area_formula(cls):
        return "π * r²"

    @classmethod
    def get_perimeter_formula(cls):
        return "2 * π * r"

