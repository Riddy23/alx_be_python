# polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape with length and width."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape with radius."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)
