#!/usr/bin/python3
"""
This module defines a function that prints a text with 
2 new lines after each of these characters: '.', '?', ':'
"""


def text_indentation(text):
    """
    Function print two new lines after character: '.', '?', ':'

    Args:
        text: parameter

    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
