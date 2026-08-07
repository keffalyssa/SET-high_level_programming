#!/usr/bin/python3
"""Unittests for models/square.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        """Reset Base ID before each test"""
        Base._Base__nb_objects = 0

    def test_square_is_rectangle(self):
        """Test that Square is an instance of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_one_arg(self):
        """Test Square with one argument"""
        s = Square(10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_square_size_getter(self):
        """Test Square size getter"""
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_square_size_setter(self):
        """Test Square size setter"""
        s = Square(10)
        s.size = 20
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_square_area(self):
        """Test Square area calculation"""
        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_square_str(self):
        """Test Square string representation"""
        s = Square(10, 0, 0, 1)
        expected = "[Square] (1) 0/0 - 10"
        self.assertEqual(str(s), expected)

    def test_square_update_args(self):
        """Test Square update with args"""
        s = Square(10, 0, 0, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_square_to_dictionary(self):
        """Test Square to_dictionary method"""
        s = Square(10, 2, 3, 1)
        d = s.to_dictionary()
        self.assertEqual(d['id'], 1)
        self.assertEqual(d['size'], 10)


if __name__ == '__main__':
    unittest.main()
