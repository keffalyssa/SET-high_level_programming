#!/usr/bin/python3
"""Base class for geometric shapes"""
import json


class Base:
    """Base class for Rectangle and Square"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """Return JSON string representation of list_dicts"""
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries from JSON string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dummy):
        """Return instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None
        dummy_instance.update(**dummy)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return list of instances loaded from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                list_instances = []
                for dictionary in list_dicts:
                    list_instances.append(cls.create(**dictionary))
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string of list_objs to file"""
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            json_string = "[]"
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_string)
