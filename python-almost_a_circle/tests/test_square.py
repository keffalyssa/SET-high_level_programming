#!/usr/bin/python3
"""Unittests for models/square.py"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_1_exists(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2_exists(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3_exists(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_string_exists(self):
        with self.assertRaises(TypeError):
            Square('1')

    def test_square_string_x_exists(self):
        with self.assertRaises(TypeError):
            Square(1, '2')

    def test_square_string_y_exists(self):
        with self.assertRaises(TypeError):
            Square(1, 2, '3')

    def test_square_1_2_3_4_exists(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_negative_exists(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x_exists(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y_exists(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_exists(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_for_square_exists(self):
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(str(s), str)
        self.assertIn("[Square]", str(s))

    def test_to_dictionary_in_square_exists(self):
        s = Square(1, 2, 3, 4)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)

    def test_create_id_exists(self):
        s = Square.create(**{ 'id': 89 })
        self.assertEqual(s.id, 89)

    def test_create_id_size_exists(self):
        s = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s.size, 1)

    def test_create_id_size_x_exists(self):
        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y_exists(self):
        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s.y, 3)

    def test_square_save_to_file_none_exists(self):
        try:
            Square.save_to_file(None)
        except Exception as e:
            self.fail(f"save_to_file(None) raised {type(e).__name__}")

    def test_square_save_to_file_empty_list_exists(self):
        try:
            Square.save_to_file([])
        except Exception as e:
            self.fail(f"save_to_file([]) raised {type(e).__name__}")

    def test_square_save_to_file_exists(self):
        s = Square(1)
        try:
            Square.save_to_file([s])
        except Exception as e:
            self.fail(f"save_to_file([s]) raised {type(e).__name__}")

    def test_load_from_file_when_file_doesnt_exist_exists(self):
        result = Square.load_from_file()
        self.assertIsInstance(result, list)

    def test_load_from_file_when_file_exists_exists(self):
        s = Square(1)
        Square.save_to_file([s])
        result = Square.load_from_file()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
