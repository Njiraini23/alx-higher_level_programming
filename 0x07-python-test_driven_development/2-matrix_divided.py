#!/usr/bin/python3
# 2-matrix_divided.py

"""A module to divide all elements of a matrix.
The module divides all the values of a matrix accoridng to a divisor given by the user.The following aspects must be taken into account:
    *Matrix should be a list of integers or floats
    *Each row must be of same size
    *Divisor must be a number (integer or float other than 0
    *The result is delivered to a new matrix.
"""
def matrix_divided(matrix, div):
    """A function that divides the integer/float nubers of a matrix
    Args:
        matrix: list of the elements of integers/floats
        div: the number to divide the matrix
    Returns:
        A new matrix with result of the division
    Raises:
        TypeError: If the elements of the matrix arent lists
                    If the elements of the lists arent integers/floats
                    If div is not an integer/float number
                    If the lists of the matrix dont have the same size
        ZerroDivisionError: if div is zero
        """

        if not type(div) in (int, float):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"

        if not matrix or not isinstance(matrix, list):
            raise TypeError(matrix_msg)
        
        len_elem = 0
        msg_size = "Each row of the matrix have the same size"

        for elements in matrix:
            if not elements or not isinstance(elements, list):
                raise TypeError(matrix_msg)

            if len_elem != 0 and len(elements) != len_elem:
                raise TypeError(msg_size)

            for num in elements:
                if not type(num) in (int, float):
                raise TypeError(matrix_msg)
        
        len_elem = len(elements)

    i = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (i)
