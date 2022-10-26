#!/usr/bin/python3
"""class square inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Square class inheriting from BaseGeometry"""

    def __init__(self, size):
        """Initialize Square object
        Args:
            size: square size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size * self.__size
