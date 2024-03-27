from shape import Shape
import math

class Pentagon(Shape):
    def __init__(self, a):
        if a <= 0:
            raise ValueError("length must be positive")
        self.a = a

    def get_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a ** 2

    def get_perimeter(self):
        return 5 * self.a

    def __str__(self):
        return f"Pentagon with side length {self.a}"

    @classmethod
    def get_area_formula(cls):
        return "(1/4) * √(5 * (5 + 2 * √5)) * side length²"

    @classmethod
    def get_perimeter_formula(cls):
        return "5 * side length"
