#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size=None):
    """Prints a square with the character #.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if size is None:
        raise TypeError("print_square() missing 1 required positional argument: 'size'")

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print("#" * size)
