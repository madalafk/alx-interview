#!/usr/bin/python3
"""
Pascal's Triangle

This script defines a function to generate Pascal's triangle up to a specified
number of rows.

Usage:
    To use this script, import the pascal_triangle function and call it with
    the desired number of rows.

"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
