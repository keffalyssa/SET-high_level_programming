#!/usr/bin/python3
"""Defines the Base model class."""


class Base:
    """Represent the base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation."""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
