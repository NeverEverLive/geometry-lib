import math
import pytest
from exceptions.shape import InvalidShape
from geometry import Triangle


def test_triangle_area():
    assert math.isclose(Triangle(3, 4, 5).area(), 6.0, rel_tol=1e-5)


def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.is_right_angled()


def test_not_right_triangle():
    t = Triangle(3, 3, 3)
    assert not t.is_right_angled()


def test_invalid_triangle():
    with pytest.raises(InvalidShape):
        Triangle(1, 2, 3)


def test_negative_side():
    with pytest.raises(InvalidShape):
        Triangle(3, -4, 5)
