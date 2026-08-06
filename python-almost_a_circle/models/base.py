#!/usr/bin/python3
"""Defines the Base model class."""


class Base:
    """Represent the base model.

    Attributes:
        __nb_instances (int): The number of instantiated Bases.
        id (int): A unique identifier.
    """

    __nb_instances = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_instances += 1
            self.id = Base.__nb_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
