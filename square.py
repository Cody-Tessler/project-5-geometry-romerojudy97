"""
Implement this class.
Recall that every square is a rectangle.
Therefore the Square class should inherit from the Rectangle class.
Do NOT implement the get_area() and get_perimeter() methods here.
Those methods should be inherited from the parent class.
"""
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, a):
        self.length = a
        self.width = a
        if a < 0:
            raise ValueError("Side length must be non-negative")
        # super().__init__(a, a)  # Initialize length and width using the parent class constructor

    def __str__(self):
        return f"Square with side length {self.length:.2f}"

    @classmethod
    def get_area_formula(cls):
        return "side length * side length"

    @classmethod
    def get_perimeter_formula(cls):
        return "4 * side length"
