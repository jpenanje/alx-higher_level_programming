#!/usr/bin/python3
"""class Rectangle inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle object
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """return print() and str() representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
