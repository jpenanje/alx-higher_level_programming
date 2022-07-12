#!/usr/bin/python3
"""Create class called Rectangle"""


class Rectangle:
    """
    Define a rectangle using width and height
    """
    def __init__(self, width=0,height=0):
        """
        Instantiate the class
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width=width
        self.height=height

    @property
    def width(self):
        """retrieve width
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Args:
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
