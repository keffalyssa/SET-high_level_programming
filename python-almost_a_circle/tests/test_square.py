#!/usr/python3
"""Unit tests for Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_is_rectangle(self):
        """Test inheritance from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_size_accessor(self):
        """Test size getter and setter."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_invalid_size(self):
        """Test invalid size types and values."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
