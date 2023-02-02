#!/usr/bin/python
"""Module "0-add_integer" that adds two integers (a, b)"""


def add_integer(a, b=98):
    """ Return sum of two numbers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
