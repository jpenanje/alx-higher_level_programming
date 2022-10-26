#!/usr/bin/python3
"""Subclass of class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an inherited instance of a class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if object is an inherited instance of a class
        Else False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
