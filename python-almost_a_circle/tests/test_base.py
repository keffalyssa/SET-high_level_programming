#!/usr/bin/python3
"""Unittests for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Reset Base ID before each test"""
        Base._Base__nb_objects = 0

    def test_id_not_provided(self):
        """Test Base() for assigning automatically an ID exists"""
        b = Base()
        self.assertIsNotNone(b.id)

    def test_id_increment(self):
        """Test Base() for assigning automatically an ID + 1"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_passed(self):
        """Test Base(89) saving the ID passed exists"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None) exists"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        """Test of Base.to_json_string([]) exists"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_dict(self):
        """Test of Base.to_json_string([{'id': 12}]) exists"""
        dict_list = [{'id': 12}]
        result = Base.to_json_string(dict_list)
        self.assertIsInstance(result, str)
        self.assertIn('12', result)

    def test_to_json_string_dict_returning_string(self):
        """Test of Base.to_json_string([{'id': 12}]) returning a string exists"""
        dict_list = [{'id': 12}]
        result = Base.to_json_string(dict_list)
        self.assertEqual(type(result), str)

    def test_from_json_string_none(self):
        """Test of Base.from_json_string(None) exists"""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty_string(self):
        """Test of Base.from_json_string('[]') exists"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_dict(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') exists"""
        json_str = '[{ "id": 89 }]'
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)

    def test_from_json_string_dict_returning_list(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') returning a list exists"""
        json_str = '[{ "id": 89 }]'
        result = Base.from_json_string(json_str)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 89)


if __name__ == '__main__':
    unittest.main()
