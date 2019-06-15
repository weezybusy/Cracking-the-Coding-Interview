#!/usr/bin/env python3

"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in
the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you
do this in place?
"""

# Check if the provided matrix is 4Nx4N.
def is_4n_x_4n(matrix):
    n = len(matrix)
    if n == 0 or n % 4 != 0:
        return False
    for i in range(n):
        if len(matrix[i]) != n:
            return False
    return True


# Time complexity:  O(n^2).
# Space complexity: O(n).
def rotate_matrix(matrix):

    if not is_4n_x_4n(matrix):
        return None

    n = len(matrix)
    new_matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[n-1-j][i]

    return new_matrix


# Time complexity:  O(n^2).
# Space complexity: O(1).
def rotate_matrix_in_place(matrix):

    if not is_4n_x_4n(matrix):
        return False

    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save top.
            top = matrix[first][i]

            # left -> top.
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left.
            matrix[last-offset][first] = matrix[last][last-offset]

            # right -> bottom.
            matrix[last][last-offset] = matrix[i][last]

            # top -> right.
            matrix[i][last] = top
    return True
