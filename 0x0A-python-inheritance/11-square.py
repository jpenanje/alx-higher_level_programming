#!/usr/bin/python3
"""class square inherits BaseGeometry"""
BaseGeometry = __import__('9-base_geometry').BaseGeometry


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
    
    def __str__(self):
        """return print() and str() representation of square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
