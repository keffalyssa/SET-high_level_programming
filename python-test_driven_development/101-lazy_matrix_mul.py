#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using the NumPy module."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    try:
        res = np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    return res
