import math
import pytest
from exceptions.shape import InvalidShape
from geometry import Circle


def test_circle_area():
    assert math.isclose(Circle(2).area(), math.pi * 4, rel_tol=1e-5)


def test_circle_negative():
    with pytest.raises(InvalidShape):
        Circle(-1)
