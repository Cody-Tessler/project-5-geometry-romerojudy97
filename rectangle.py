from shape import Shape
import math
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length {self.length:.2f} and width {self.width:.2f}"

    @classmethod
    def get_area_formula(cls):
        return "length × width"

    @classmethod
    def get_perimeter_formula(cls):
        return "2 × (length + width)"