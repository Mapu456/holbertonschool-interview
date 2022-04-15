#!/usr/bin/python3
"""
contains the Pascal's Triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    triangle = []
    aux = 0

    for i in range(n):
        triangle.append([])

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                aux = triangle[i - 1][j] + triangle[i - 1][j - 1]
                triangle[i].append(aux)

    return triangle
