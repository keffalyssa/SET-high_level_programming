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

    def test_type_error_width(self):
        """Test Rectangle("1", 2) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_type_error_height(self):
        """Test Rectangle(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_type_error_x(self):
        """Test Rectangle(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_type_error_y(self):
        """Test Rectangle(1, 2, 3, "4") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_error_width_negative(self):
        """Test Rectangle(-1, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_value_error_height_negative(self):
        """Test Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)


if __name__ == "__main__":
    unittest.main()
