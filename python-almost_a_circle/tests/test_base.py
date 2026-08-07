#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for the Base class"""

    def test_id_not_provided(self):
        """Test Base() for assigning automatically an ID exists"""
        b = Base()
        self.assertIsNotNone(b.id)

    def test_id_increment(self):
        """Test Base() for assigning automatically an ID + 1 of the previous exists"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_passed(self):
        """Test Base(89) saving the ID passed exists"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None) exists"""
        res = Base.to_json_string(None)
        self.assertEqual(res, "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([]) exists"""
        res = Base.to_json_string([])
        self.assertEqual(res, "[]")

    def test_to_json_string_dict(self):
        """Test Base.to_json_string([ { 'id': 12 }]) exists"""
        res = Base.to_json_string([{'id': 12}])
        self.assertEqual(res, '[{"id": 12}]')
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None) exists"""
        res = Base.from_json_string(None)
        self.assertEqual(res, [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("[]") exists"""
        res = Base.from_json_string("[]")
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()
