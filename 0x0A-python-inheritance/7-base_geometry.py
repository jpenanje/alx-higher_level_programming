#!/usr/bin/python3
"""Define a base geometry class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate an integer and integer must be greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
