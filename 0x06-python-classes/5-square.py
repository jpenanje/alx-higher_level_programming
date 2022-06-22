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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def area(self):
        """Calculate area of square
        Returns:
            area of square
        """
        return (self.__size**2)

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.area() + 1):
                if i % self.__size != 0:
                    print("#", end="")
                else:
                    print("#")
