#!/usr/bin/python3
"""Create a class square"""


class Square:
    """A Square class that defines a square by it's size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square
        Args:
            size: size of square
            position: postion of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 " + 
            "positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set size
        Args:
            value: value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position of square"""
        return self.__position

    @postion.setter
    def position(self, value):
        """set square position"""
        if position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 " +
            "positive integers")
        self.__position = value

    def area(self):
        """Calculate area of square
        Returns:
            area of square
        """
        return (self.__size**2)

    def my_print(self):
        """print in stdout square with character #"""
        if self.__size == 0:
            print()
        else:

