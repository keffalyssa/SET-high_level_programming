#!/usr/python3
"""Unit tests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_is_base(self):
        """Test inheritance from Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_width_types(self):
        """Test invalid width types."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 2)

    def test_width_values(self):
        """Test invalid width values."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
