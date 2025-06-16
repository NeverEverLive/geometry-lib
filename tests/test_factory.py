import math
import pytest
from exceptions.shape import InvalidShape
from geometry import Circle, Triangle, get_shape
from geometry.base import Shape


def test_factory_circle():
    Circle(2)
    shape = get_shape("circle", 1)
    assert isinstance(shape, Circle)
    assert math.isclose(shape.area(), math.pi, rel_tol=1e-5)


def test_factory_triangle():
    shape = get_shape("triangle", 3, 4, 5)
    assert isinstance(shape, Triangle)
    assert shape.is_right_angled()


def test_custom_shape_registration():
    class Foo(Shape):
        def area(self) -> float:
            return 42.0

    shape = get_shape("Foo")
    assert isinstance(shape, Foo)
    assert shape.area() == 42.0


def test_unknown_shape():
    with pytest.raises(InvalidShape):
        get_shape("hexagon", 1, 1, 1, 1, 1, 1)
