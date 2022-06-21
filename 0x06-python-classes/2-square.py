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
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
