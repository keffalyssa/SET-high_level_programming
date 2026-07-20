#!/usr/bin/python3
"""Defines a MagicClass that matches given Python bytecode."""
import math


class MagicClass:
    """Represents a circle-like magic class with radius, area, and circumference."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the circumference."""
        return 2 * math.pi * self.__radius
