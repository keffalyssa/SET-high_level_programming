#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for testing the Rectangle class."""

    def test_rectangle_exists(self):
        """Test Rectangle(1, 2) exists."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_three_args(self):
        """Test Rectangle(1, 2, 3) exists."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_four_args(self):
        """Test Rectangle(1, 2, 3, 4) exists."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
