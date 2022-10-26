#!/usr/bin/python3
"""class square inherits Rectangle"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

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
