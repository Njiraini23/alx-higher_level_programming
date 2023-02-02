!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    class defined with private
    instance attritbute: size
    """
    def __init__(self, size=0):
        """
        Args:
            size: initialize size
            """
        if type(size) is int:
            if size < 0:
                raise ValueError("Size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        finds area of square
        Returns: area of the square
        """
        return self.__size ** 2
