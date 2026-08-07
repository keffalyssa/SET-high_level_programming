#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update Square attributes"""
        if args and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == 'size':
                        self.size = arg
                    else:
                        setattr(self, attrs[i], arg)
        else:
            if 'size' in kwargs:
                self.size = kwargs['size']
            for key, value in kwargs.items():
                if key != 'size' and hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
