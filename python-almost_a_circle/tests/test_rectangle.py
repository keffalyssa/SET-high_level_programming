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

    def test_rectangle_five_args(self):
        """Test Rectangle(1, 2, 3, 4, 5) exists."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_value_error_width_zero(self):
        """Test Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_value_error_height_zero(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_value_error_x_negative(self):
        """Test Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_value_error_y_negative(self):
        """Test Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area() method exists and returns correct value."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)


if __name__ == "__main__":
    unittest.main()
