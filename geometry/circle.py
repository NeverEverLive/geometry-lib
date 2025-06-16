import math
from exceptions.shape import InvalidShape
from geometry.base import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise InvalidShape("Radius cannot be negative.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
