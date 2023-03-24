#!/usr/bin/python3
"""
comment
"""


def pascal_triangle(n):
    """
    comment
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for item in range(n-1):
        pascal.append(
            [i+j for i, j in zip([0] + pascal[-1], pascal[-1] + [0])])

    return pascal
