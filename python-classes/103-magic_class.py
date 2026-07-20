#!/usr/bin/python3
"""Defines a MagicClass."""
import math


class MagicClass:
    """Represents a circle-like magic class."""

    def __init__(self, radius=0):
        """Initialize the MagicClass."""
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
