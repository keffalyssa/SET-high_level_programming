#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_1_2_exists(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3_exists(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4_exists(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_1_2_3_4_5_exists(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_string_width_exists(self):
        with self.assertRaises(TypeError):
            Rectangle('1', 2)

    def test_rectangle_string_height_exists(self):
        with self.assertRaises(TypeError):
            Rectangle(1, '2')

    def test_rectangle_negative_width_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y_exists(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_display_without_x_y_exists(self):
        r = Rectangle(1, 2)
        r.display()

    def test_display_without_y_exists(self):
        r = Rectangle(1, 2, 3)
        r.display()

    def test_display_exists(self):
        r = Rectangle(1, 2, 3, 4)
        r.display()

    def test_to_dictionary_exists(self):
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)

    def test_update_exists(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_create_id_exists(self):
        r = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r.id, 89)

    def test_create_id_width_exists(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r.width, 1)

    def test_create_id_width_height_exists(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x_exists(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y_exists(self):
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r.y, 4)

    def test_save_to_file_none_exists(self):
        Rectangle.save_to_file(None)

    def test_save_to_file_empty_list_exists(self):
        Rectangle.save_to_file([])

    def test_save_to_file_exists(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])

    def test_load_from_file_when_file_doesnt_exist_exists(self):
        result = Rectangle.load_from_file()
        self.assertIsInstance(result, list)

    def test_load_from_file_when_file_exists_exists(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
