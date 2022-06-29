#!/usr/bin/python3
"""Module that prints a first and last name"""


def say_my_name(first_name, last_name=""):
    """
    prints first and last name

    Args:
        first_name: first parameter
        last_name: second parameter

    Raises:
        TypeError: first and last name must be strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
