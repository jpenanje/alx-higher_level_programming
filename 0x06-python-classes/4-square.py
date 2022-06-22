#!/usr/bin/python3
"""Create a class called Square"""


class Square:
    """A Square class that defines a square by it's size
    """
    def __init__(self, size=0):
        """Instantiate a square
        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size
        Args:
            value: value of size
        """
        if type(size) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate area of square
        Returns:
            area of square
        """
        return (self.__size**2)
