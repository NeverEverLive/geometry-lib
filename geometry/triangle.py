import math
from exceptions.shape import InvalidShape
from geometry.base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise InvalidShape("Sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise InvalidShape("Sides must form a triangle.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)
