#!/usr/bin/python3
"""module that defines 'add_integer' that adds two numbers"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b
    
    Args:
        a: first parameter
        b: second parameter
    
    Raises:
        TypeError: a and b must be integers

    Returns:
        sum of a and b
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
