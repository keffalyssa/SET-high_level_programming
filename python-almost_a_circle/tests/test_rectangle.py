#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset Base ID before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_is_base(self):
        """Test that Rectangle is an instance of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_no_args(self):
        """Test Rectangle with no arguments raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        """Test Rectangle with one argument raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_two_args(self):
        """Test Rectangle with two arguments"""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_rectangle_width_getter(self):
        """Test width getter"""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)

    def test_rectangle_height_getter(self):
        """Test height getter"""
        r = Rectangle(10, 5)
        self.assertEqual(r.height, 5)

    def test_rectangle_area(self):
        """Test Rectangle area calculation"""
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_rectangle_str(self):
        """Test Rectangle string representation"""
        r = Rectangle(10, 5, 0, 0, 1)
        expected = "[Rectangle] (1) 0/0 - 10/5"
        self.assertEqual(str(r), expected)

    def test_rectangle_update_args(self):
        """Test Rectangle update with args"""
        r = Rectangle(10, 5, 0, 0, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_to_dictionary(self):
        """Test Rectangle to_dictionary method"""
        r = Rectangle(10, 5, 2, 3, 1)
        d = r.to_dictionary()
        self.assertEqual(d['id'], 1)
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 5)


if __name__ == '__main__':
    unittest.main()
