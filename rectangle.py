from shape import Shape

class Rectangle(Shape):

    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        area = self.get_area()
        perimeter = self.get_perimeter()
        return f"Rectangle with length {self.length} and width {self.width}, Area: {area}, Perimeter: {perimeter}"

    @classmethod
    def get_area_formula(cls):
        return "length * width"

    @classmethod
    def get_perimeter_formula(cls):
        return "2 * (length + width)"
