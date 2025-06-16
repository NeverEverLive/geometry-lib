from typing import Any

from exceptions.shape import InvalidShape
from geometry.base import ShapeMeta, Shape

def get_shape(shape_type: str, *args: Any, **kwargs: Any) -> Shape:
    shape_type = shape_type.lower()
    registry = ShapeMeta.get_registry()
    cls = registry.get(shape_type)
    if cls is None:
        raise InvalidShape(f"Unknown shape: {shape_type}")
    return cls(*args, **kwargs)
