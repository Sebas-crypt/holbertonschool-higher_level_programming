#!/usr/bin/python3
"""this script creates a subclass called square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string representation of the instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """retrieves the width attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size attributes"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes of the instance"""
        if args and len(args) != 0:
            list_length = len(args)
            self.id = args[0]
            i = 1
            while i < list_length:
                if i == 1:
                    if not isinstance(args[1], int):
                        raise TypeError("size must be an integer")
                    if args[1] <= 0:
                        raise ValueError("size must be > 0")
                    self.size = args[1]
                if i == 2:
                    if not isinstance(args[2], int):
                        raise TypeError("x must be an integer")
                    if args[2] < 0:
                        raise ValueError("x must be >= 0")
                    self.x = args[2]
                if i == 3:
                    if not isinstance(args[3], int):
                        raise TypeError("y must be an integer")
                    if args[3] < 0:
                        raise ValueError("y must be >= 0")
                    self.y = args[3]
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id is not an integer")
                    self.id = value
                if key == "size":
                    if not isinstance(value, int):
                        raise TypeError("size must be an integer")
                    if value <= 0:
                        raise ValueError("size must be > 0")
                    self.size = value
                if key == "x":
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.x = value
                if key == "y":
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the class instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
