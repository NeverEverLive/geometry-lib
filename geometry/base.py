from abc import ABC, abstractmethod, ABCMeta
import logging
from typing import Type, Dict


class ShapeMeta(ABCMeta):
    _registry: Dict[str, Type["Shape"]] = {}

    def __new__(cls, name, bases, namespace, **kwargs):
        logging.warning(name)
        cls = super().__new__(cls, name, bases, namespace)
        if name != "shape":
            shape_name = name.lower()
            cls._registry[shape_name] = cls
        return cls

    @classmethod
    def get_registry(cls):
        return dict(cls._registry)


class Shape(ABC, metaclass=ShapeMeta):
    """Base abstract class for geometry figures."""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the figure."""
        pass
