import math


class Shape:
    def area(self):
        ...
    
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * math.pi ** 2
    
    def perimeter(self):
        return self.radius * math.pi * 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def __eq__(self, other):
        return (
            self.length == other.length and self.width == other.width
            if isinstance(other, Rectangle)
            else False
        )

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
