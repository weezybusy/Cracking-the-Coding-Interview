#!/usr/bin/env python3


"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""


# Time complexity:  O(mn).
# Space complexity: O(mn).
def zero_matrix(matrix):

    m = len(matrix)
    n = len(matrix[0])
    zero_rows = []
    zero_cols = []

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row not in zero_rows:
                    zero_rows.append(row)
                if col not in zero_cols:
                    zero_cols.append(col)

    for row in range(m):
        for col in range(n):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0
