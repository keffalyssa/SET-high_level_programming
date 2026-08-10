#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices by using the NumPy module.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.
    """
    return np.matmul(m_a, m_b)
