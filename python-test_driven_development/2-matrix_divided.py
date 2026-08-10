#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of ints/floats): The matrix to divide.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with the results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats,
                   if rows are empty, if rows are of different sizes,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(len(row) > 0 for row in matrix) or
            not all(all(isinstance(ele, (int, float)) for ele in row)
                    for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
