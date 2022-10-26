#!/usr/bin/python3
"""Is an instance or not of a specified class"""


def is_same_class(obj, a_class):
    """
    check if an object is an instance of a given class
    Args:
        obj: the object to check
        a_class: the parent class
    Returns:
        True if object isinstance of a_class
        else False
    """
    if type(obj) == a_class:
        return True
    return False
