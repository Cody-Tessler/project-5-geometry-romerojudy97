from shape import Shape
import math

class Pentagon(Shape):
    def __init__(self, a):
        self.side_length = a

    def get_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2

    def get_perimeter(self):
        return 5 * self.side_length

    def __str__(self):
        return f"Pentagon with side length {self.side_length:.2f}"

    @classmethod
    def get_area_formula(cls):
        return "(1/4) * √(5 * (5 + 2 * √5)) * a²"

    @classmethod
    def get_perimeter_formula(cls):
        return "5 * a"
