#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    create triangle
    """
    import math
    fact = math.factorial
    i = 0
    T = []
    if n <= 0:
        return T
    while i < n:
        row = [fact(i) // (fact(j) * fact(i - j)) for j in range(0, i + 1)]
        T.append(row)
        i = i + 1
    return T
