#!/usr/bin/python3
"""a class square that defines a square by:
    Private instance attribute: size
    instantiation with size(no type/value verification)
    You are not allwoed to import any module
"""


class Square:
    """Represent a square."""
    def __int__(self, size):
        """__init__
        The __int__method initializes the size value
        of  the square.
        Attritbues:
            size (int): The size of the square.
            """
        self.__size = size
