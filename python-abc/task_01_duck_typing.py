#!/usr/bin/python3
"""Shapes module."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info."""
    try:
        print("Area: {}".format(shape.area()))
        print("Perimeter: {}".format(shape.perimeter()))
    except AttributeError:
        pass
