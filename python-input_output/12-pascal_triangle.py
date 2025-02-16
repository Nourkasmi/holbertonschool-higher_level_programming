#!/usr/bin/python3
"""
Returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle
