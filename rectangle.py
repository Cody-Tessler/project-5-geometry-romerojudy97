from shape import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Length and width must be non-negative")
        self.a = a  # Assign a to self.a
        self.b = b  # Assign b to self.b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        area = self.get_area()
        perimeter = self.get_perimeter()
        return f"Rectangle with length {self.a} and width {self.b}, Area: {area}, Perimeter: {perimeter}"

    @classmethod
    def get_area_formula(cls):
        return "a * b"

    @classmethod
    def get_perimeter_formula(cls):
        return "2 * (a + b)"
